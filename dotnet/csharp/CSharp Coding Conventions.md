---
kind: reprint
source: site:medium.com
---

# C# Coding Conventions


![img](https://miro.medium.com/v2/resize:fit:875/1*TLfTMEdLHAdSnj24v5Vqdw.png)

# Namespace

- **DO use PascalCase for namespace**

```csharp
// CORRECT:
namespace Xtramile.Application.Services;// WRONG:
namespace Xtramile.application.services;
```

- **DO use “noun” for namespace**

```csharp
// CORRECT: “Entites” is a noun 
namespace Xtramile.Application.Entities;// WRONG: “CreateEntity” is a verb
namespace Xtramile.Application.CreateEntity;
```

- **DO use “plural word” for namespace**

```csharp
// CORRECT: “Services” is plural
namespace Xtramile.Application.Services;// WRONG: “Service” is singular
namespace Xtramile.Application.Service;
```

- **DO use file-scoped namespace declaration if using C#10 or higher**

```csharp
// C#10 or higher
namespace Xtramile.Application.Services;

// C# 9 or lower
namespace Xtramile.Application.Services
{
    // ...
}
```

- **DON’T use underscore for namespace**
- **DON’T exceed 100 characters length for namespace name**

# Class

- **DO use PascalCase for class name**

```csharp
public class UserService
{
    // ....
}
```

- **DO use “noun” for class name**

```csharp
/ CORRECT: DataInitializer is a noun
public class DataInitializer
{
    // ...
}

// WRONG: InitializeData is a verb
public class InitializeData
{
    // ...
}
```

- **DO use “singular word” for class name**

```csharp
// CORRECT
public class UserService
{
    // ...
}

// WRONG: UserServices is plural
public class UserServices
{
    // ...
}
```

- **DO vertically aligned curly brackets**

```csharp
// CORRECT
public class UserService
{
    // ...
}

// WRONG
public class UserService {
    // ...
}
```

- **DON’T use underscore for class name**

```csharp
// WRONG
public class User_Service
{
    // ...
}
```

- **DON’T exceed 100 characters length for class name**

# Interface

- **DO use PascalCase for interface name**

```csharp
public interface IUserService
{
    // ...
}
```

- **DO use “noun” for interface name**

```csharp
// CORRECT: "DataGenerator" is a noun
public interface IDataGenerator
{
    // ...
}

// WRONG: "GenerateData" is a verb
public interface IGenerateData
{
    // ...
}
```

- **DO prefix interface with the letter “I”**

```csharp
// CORRECT
public interface IDataContext
{
    // ...
}

// WRONG
public interface DataContext
{
    // ...
}
```

- **DO vertically aligned curly brackets**

```csharp
// CORRECT
public interface IUserService
{
    // ...
}

// WRONG
public interface IUserService {
    // ...
}
```

- **DON’T use underscore for interface name**
- **DON’T exceed 100 characters length for interface name**

# Constant

- **DO use PascalCase for constant name**

```csharp
public const string BaseUrl = "https://api.example.com";
```

- **DO use “noun” for constant name**

```csharp
// CORRECT
public const bool IsRunning = true;

// WRONG
public const bool Run = true;
```

- **DO use meaningful words for constant name**

```csharp
// CORRECT
public const string UserConfig = "UserConfig";

// WRONG
public const string UsrCfg = "UsrCfg";
```

- **DO use predefined type name (int, string, float) instead of .NET type (Int32, String, Single) for constant declarations**

```csharp
// CORRECT: "string" is predefined type name
public const string BaseUrl = "https://api.example.com";

// WRONG: "String" is .NET type
public const String BaseUrl = "https://api.example.com";
```

- **DON’T use underscore for constant name**

```csharp
// CORRECT
public const string BaseUrl = "https://api.example.com";

// WRONG
public const string Base_Url = "https://api.example.com";
```

- **DON’T use SCREAMINGCASE for constant name**

```csharp
// CORRECT
public const int MaximumFileSize = 1024;

// WRONG: imagine what will happen if you send ALL CAPS message to your partner
public const string MAXIMUM_FILE_SIZE = 1024;
```

- **DON’T use uncommon abbreviations for constant name**

```csharp
// CORRECT: "Url" is common abbreviation
public const string BaseUrl = "https://api.example.com";

// CORRECT: "Xml" is common abbreviation
public const string XmlFileLocation = "C:\\xml";

// WRONG: "usr", "svc", "cfg" are uncommon abbreviations
public const string UsrSvcCfgLoc = "c:\\xml";
```

- **DON’T use Hungarian notation for constant name**

```csharp
// WRONG: do not use prefix str
public const string strConfig = "strConfig";

// WRONG: do not use prefix txt
public const string txtUserName = "txtUserName";
```

- **DON’T exceed 50 characters length for constant name**

# Field

- **DO use camelCase for field name**

```csharp
// CORRECT
private int _age = 30;

// WRONG
private int Age = 30;
```

- **DO use “noun” for field name**

```csharp
// CORRECT
private int _isRunning = false;

// WRONG: "Run" is a verb
private int _run = false;
```

- **DO prefix fields with the underscore symbol**

```csharp
private string _name = "";
```

- **DO use meaningful words for field name**

```csharp
// CORRECT
private readonly IUserService _userService;

// WRONG
private readonly IUserService _usrSvc;
```

- **DO use predefined type name (int, string, float) instead of .NET type (Int32, String, Single) for field declarations**

```csharp
// CORRECT
private int _age = 30;

// WRONG
private Int32 _age = 30;
```

- **DO make field as readonly if possible**

```csharp
private readonly IUserService _userService;
```

- **DON’T use uncommon abbreviations for field name**

```csharp
// WRONG
private readonly int _usrMaxLmtSzMin = 10;
```

- **DON’T use Hungarian notation for field name**

```csharp
// WRONG: do not use prefix "txt"
private string _txtName = "txtName";
```

- **DON’T exceed 50 characters length for field name**

# Property

- **DO use PascalCase for property name**

```csharp
// CORRECT
public string FirstName { get; set; }

// WRONG: we will never use snake_case
public string first_name { get; set; }
```

- **DO use “noun” for property name**

```csharp
// CORRECT
public bool IsDeleted { get; set; }

// WRONG: delete is a "verb"
public bool Delete { get; set; }
```

- **DO use meaningful words for property name**

```csharp
// CORRECT
public string FirstName { get; set; }
public string LastName { get; set; }

// WRONG
public string FN { get; set; }
public string LN { get; set; }
```

- **DO use predefined type name (int, string, float) instead of .NET type (Int32, String, Single) for property declarations**

```csharp
// CORRECT
public float Weight { get; set; }

// WRONG
public Single Weight { get; set; }
```

- **DON’T use uncommon abbreviations for property name**

```csharp
// CORRECT
public string PostCode { get; set; }

// WRONG
public string PstCde { get; set; }
```

- **DON’T use Hungarian notation for property name**

```csharp
// CORRECT
public string Name { get; set; }

// WRONG
public string strName { get; set; }
```

- **DON’T exceed 50 characters length for property name**

# Method

- **DO use PascalCase for method name**

```csharp
// CORRECT
public void CreateUser(string username)
{
    // ...
}

// WRONG
public void createUser(string username)
{
    // ...
}
```

- **DO use “verb” for method name**

```csharp
// CORRECT: "CreateUser" is a verb
public void CreateUser(string username)
{
    // ...
}

// WRONG: "UserCreator" is a noun
public void UserCreator(string username)
{
    // ...
}
```

- **DO vertically aligned curly brackets**

```csharp
// CORRECT
public void CreateUser(string username)
{
    // ...
}

// WRONG
public void CreateUser(string username) {
    // ...
}
```

- **DON’T use underscore for method name**
- **DON’T exceed 50 characters length for method name**

# Method Arguments

- **DO use camelCase for method arguments**

```csharp
// CORRECT
public void Login(string firstName, string lastName)
{
    // ...
}

// WRONG: "first_name" is snake_case; "LastName" is PascalCase
public void Login(string first_name, string LastName)
{
    // ...
}
```

- **DO use “noun” for method arguments**

```csharp
// CORRECT: "deletedId" is a noun
public void Delete(int deletedId)
{
    // ...
}

// WRONG: "deleteId" is a verb
public void Delete(int deleteId)
{
    // ...
}
```

- **DO use predefined type name (int, string, float) instead of .NET types (Int32, String, Single) for method arguments**

```csharp
// CORRECT
public void CalculateBonus(string name, int age, float salary)
{
    // ...
}

// WRONG
public void CalculateBonus(String name, Int32 age, Single salary)
{
    // ...
}
```

- **DON’T use uncommon abbreviations for method arguments**

```csharp
// CORRECT
public void DeleteUser(int deletedId)
{
    // ...
}

// WRONG
public void DelUsr(int delId)
{
    // ...
}
```

- **DON’T use Hungarian notation for method arguments**

```csharp
/ CORRECT
public User GetUser(int id)
{
    // ...
}

// WRONG
public User GetUser(int intId)
{
    // ...
}
```

- **DON’T use underscore for method arguments**
- **DON’T exceed 50 characters length for method arguments**

# Local Variables

- **DO use camelCase for variable name**

```csharp
// CORRECT
var firstName = "Juldhais Hengkyawan";

// WRONG
var FirstName = "Juldhais Hengkyawan";

// WRONG
var first_name = "Juldhais Hengkyawan";
```

- **DO use “noun” for variable name**

```csharp
// CORRECT
var created = true;

// WRONG: "create" is a verb
var create = false;
```

- **DO use meaningful words for variable name**

```csharp
// CORRECT
var customerTotalSales = 100;

// WRONG
var custTotSls = 100;
```

- **DO use implicit type “var” for local variable declarations with initialization**

```csharp
// CORRECT
var userDto = new UserDto();

// WRONG
UserDto userDto = new UserDto();
```

- **DO use predefined type name (int, string, float) instead of .NET types (Int32, String, Single) for variable declarations**

```csharp
// CORRECT
int salary;

// WRONG
Int32 salary;
```

- **DON’T use uncommon abbreviations for variable name**

```csharp
// CORRECT: "csv" is a common abbrevation
var csvPath = "C:\\csv";

// WRONG: "Lmt" is uncommon abbreviation
var maxLmt = 100;
```

- **DON’T use Hungarian notation for variable name**

```csharp
// CORRECT
var city = "Bogor";

// WRONG
var strCity = "Bogor";
```

- **DON’T use underscore for variable name**
- **DON’T exceed 50 characters length for variable name**

# Enum

- **DO use PascalCase for enum name**

```csharp
// CORRECT
public enum SalesOrderStatus
{
    Open,
    Closed,
    Cancelled
}

// WRONG
public enum salesOrderStatus
{
    Open,
    Closed,
    Cancelled
}
```

- **DO use “noun” for enum name**

```csharp
// CORRECT
public enum Gender
{
    Male,
    Female,
    Others
}

// WRONG
public enum GetGender
{
    Male,
    Female,
    Others
}
```

- **DO use “singular word” for enum name**

```csharp
// CORRECT
public enum Status
{
    // ...
}

// WRONG
public enum Statuses
{
    // ...
}
```

- **DON’T use suffix “Enum” for enum name**

```csharp
// CORRECT
public enum Gender
{
    // ...
}

// WRONG
public enum GenderEnum
{
    // ...
}
```

- **DON’T use underscore for enum name**
- **DON’T exceed 50 characters length for enum name**