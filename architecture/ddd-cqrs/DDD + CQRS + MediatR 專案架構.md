---
kind: original
---

// ─────────────────────────────────────────────
// Application/HumanResources/Queries/GetEmployeeList/
// ─────────────────────────────────────────────

public class EmployeeListQuery : IRequest<PagedResult<EmployeeDto>>
{
    public int Page { get; set; } = 1;
    public int PageSize { get; set; } = 10;
    public string? Keyword { get; set; }
}

public class EmployeeListQueryHandler : IRequestHandler<EmployeeListQuery, PagedResult<EmployeeDto>>
{
    private readonly IEmployeeRepository _repository;

    public EmployeeListQueryHandler(IEmployeeRepository repository)
    {
        _repository = repository;
    }
    
    public async Task<PagedResult<EmployeeDto>> Handle(EmployeeListQuery request, CancellationToken cancellationToken)
    {
        var (items, total) = await _repository.SearchAsync(request.Keyword, request.Page, request.PageSize);
    
        var result = new PagedResult<EmployeeDto>
        {
            TotalCount = total,
            Items = items.Select(e => new EmployeeDto
            {
                Id = e.Id,
                Name = e.Name,
                Department = e.Department,
                HireDate = e.HireDate
            }).ToList()
        };
    
        return result;
    }
}

// ─────────────────────────────────────────────
// Application/Common/Models/PagedResult.cs
// ─────────────────────────────────────────────

public class PagedResult<T>
{
    public int TotalCount { get; set; }
    public List<T> Items { get; set; } = new();
}

// ─────────────────────────────────────────────
// Application/Common/Interfaces/IEmployeeRepository.cs
// ─────────────────────────────────────────────

public interface IEmployeeRepository
{
    Task<(List<Employee>, int)> SearchAsync(string? keyword, int page, int pageSize);
    Task AddAsync(Employee employee);
    Task<Employee?> GetByIdAsync(Guid id);
}

// ─────────────────────────────────────────────
// Domain/Entities/Employee.cs
// ─────────────────────────────────────────────

public class Employee
{
    public Guid Id { get; private set; }
    public string Name { get; private set; }
    public string Department { get; private set; }
    public DateTime HireDate { get; private set; }

    public Employee(Guid id, string name, string department, DateTime hireDate)
    {
        Id = id;
        Name = name;
        Department = department;
        HireDate = hireDate;
    }
}

// ─────────────────────────────────────────────
// Application/HumanResources/Queries/GetEmployeeById/
// ─────────────────────────────────────────────

public record GetEmployeeByIdQuery(Guid Id) : IRequest<EmployeeDto>;

public class GetEmployeeByIdHandler : IRequestHandler<GetEmployeeByIdQuery, EmployeeDto>
{
    private readonly IEmployeeRepository _repository;

    public GetEmployeeByIdHandler(IEmployeeRepository repository)
    {
        _repository = repository;
    }
    
    public async Task<EmployeeDto> Handle(GetEmployeeByIdQuery request, CancellationToken cancellationToken)
    {
        var employee = await _repository.GetByIdAsync(request.Id);
        if (employee == null)
            throw new NotFoundException("Employee not found");
    
        return new EmployeeDto
        {
            Id = employee.Id,
            Name = employee.Name,
            Department = employee.Department,
            HireDate = employee.HireDate
        };
    }
}

// ─────────────────────────────────────────────
// Application/HumanResources/Commands/CreateEmployee/
// ─────────────────────────────────────────────

public class CreateEmployeeDto
{
    public string Name { get; set; } = string.Empty;
    public string Department { get; set; } = string.Empty;
    public DateTime HireDate { get; set; }
}

public class CreateEmployeeValidator : AbstractValidator<CreateEmployeeDto>
{
    public CreateEmployeeValidator()
    {
        RuleFor(x => x.Name).NotEmpty();
        RuleFor(x => x.Department).NotEmpty();
        RuleFor(x => x.HireDate).LessThanOrEqualTo(DateTime.Today);
    }
}

public record CreateEmployeeCommand(CreateEmployeeDto Dto) : IRequest<Guid>;

public class CreateEmployeeHandler : IRequestHandler<CreateEmployeeCommand, Guid>
{
    private readonly IEmployeeRepository _repository;

    public CreateEmployeeHandler(IEmployeeRepository repository)
    {
        _repository = repository;
    }
    
    public async Task<Guid> Handle(CreateEmployeeCommand request, CancellationToken cancellationToken)
    {
        var dto = request.Dto;
        var employee = new Employee(Guid.NewGuid(), dto.Name, dto.Department, dto.HireDate);
    
        await _repository.AddAsync(employee);
        return employee.Id;
    }
}

// ─────────────────────────────────────────────
// Application/HumanResources/EmployeeDto.cs
// ─────────────────────────────────────────────

public class EmployeeDto
{
    public Guid Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Department { get; set; } = string.Empty;
    public DateTime HireDate { get; set; }
}

// ─────────────────────────────────────────────
// Infrastructure/Persistence/Repositories/EmployeeRepository.cs
// ─────────────────────────────────────────────

public class EmployeeRepository : IEmployeeRepository
{
    private readonly ApplicationDbContext _context;

    public EmployeeRepository(ApplicationDbContext context)
    {
        _context = context;
    }
    
    public async Task<(List<Employee>, int)> SearchAsync(string? keyword, int page, int pageSize)
    {
        var query = _context.Employees.AsQueryable();
    
        if (!string.IsNullOrWhiteSpace(keyword))
            query = query.Where(e => e.Name.Contains(keyword) || e.Department.Contains(keyword));
    
        var total = await query.CountAsync();
        var items = await query.Skip((page - 1) * pageSize).Take(pageSize).ToListAsync();
    
        return (items, total);
    }
    
    public async Task AddAsync(Employee employee)
    {
        _context.Employees.Add(employee);
        await _context.SaveChangesAsync();
    }
    
    public async Task<Employee?> GetByIdAsync(Guid id)
    {
        return await _context.Employees.FindAsync(id);
    }
}

// ─────────────────────────────────────────────
// API/Controllers/HumanResourcesController.cs
// ─────────────────────────────────────────────

[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
[ApiExplorerSettings(GroupName = "Human Resources")]
public class HumanResourcesController : ControllerBase
{
    private readonly ISender _sender;

    public HumanResourcesController(ISender sender)
    {
        _sender = sender;
    }
    
    [HttpPost("employees")]
    [ProducesResponseType(typeof(ApiResponse<Guid>), StatusCodes.Status201Created)]
    [ProducesResponseType(typeof(ApiResponse), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> Create([FromBody] CreateEmployeeDto dto)
    {
        var id = await _sender.Send(new CreateEmployeeCommand(dto));
        return CreatedAtAction(nameof(GetById), new { id }, ApiResponse.Success(id));
    }
    
    [HttpGet("employees/{id}")]
    [ProducesResponseType(typeof(ApiResponse<EmployeeDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(ApiResponse), StatusCodes.Status404NotFound)]
    public async Task<ActionResult<ApiResponse<EmployeeDto>>> GetById(Guid id)
    {
        var employee = await _sender.Send(new GetEmployeeByIdQuery(id));
        return Ok(ApiResponse.Success(employee));
    }
    
    [HttpGet("employees")]
    [ProducesResponseType(typeof(ApiResponse<PagedResult<EmployeeDto>>), StatusCodes.Status200OK)]
    public async Task<ActionResult<ApiResponse<PagedResult<EmployeeDto>>>> GetList([FromQuery] EmployeeListQuery query)
    {
        var result = await _sender.Send(query);
        return Ok(ApiResponse.Success(result));
    }
}