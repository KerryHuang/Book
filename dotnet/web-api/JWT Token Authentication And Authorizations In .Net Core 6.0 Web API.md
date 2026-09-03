---
kind: reprint
source: site:c-sharpcorner.com
---

# JWT Token Authentication And Authorizations In .Net Core 6.0 Web API


## Introduction

In this step-by-step tutorial, I will demonstrate how to use the JWT token in your web API .net core 6.0 project. This tutorial covers the following topics.

- How to create a JWT access token
- How to authorize any web API endpoint

Before we start you must be knowing the following concepts - Authentication and Authorization. According to Wikipedia,

1. Authentication - is the act of proving an assertion, such as the identity of a computer system user. In contrast with identification, the act of indicating a person or thing's identity, authentication is the process of verifying that identity.
2. Authorization - is the function of specifying access rights/privileges to resources, which is related to general information security and computer security, and to access control in particular.

## Step 1. Creating a Web API project

Let's start. First, need to open Visual Studio and create a new Project

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations.png)

Now Select Web API Template.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations1.png)

Then give a name to the solution and select the folder where want to place the solution

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations2.png)

Chose .net 6 frameworks and Authentication type as None because we are implementing custom JWT Authentications

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations3.png)

## Step 2. Install Nuget Packages

Then open Nuget Package manager and install latest version of following packages,

- Microsoft.AspNetCore.Authentication.JwtBearer
- Microsoft.IdentityModel.JsonWebTokens
- System.IdentityModel.Tokens.Jwt

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations4.png)

## Step 3. Add Model and settings

Add a new folder to your project root directory name as “Models” and a new class named “JwtSettings” and “UserTokens”.

JwtSettings.cs file,

```csharp
namespace WebApplication.Models;
public class JwtSettings {
    public bool ValidateIssuerSigningKey {
        get;
        set;
    }
    public string IssuerSigningKey {
        get;
        set;
    }
    public bool ValidateIssuer {
        get;
        set;
    } = true;
    public string ValidIssuer {
        get;
        set;
    }
    public bool ValidateAudience {
        get;
        set;
    } = true;
    public string ValidAudience {
        get;
        set;
    }
    public bool RequireExpirationTime {
        get;
        set;
    }
    public bool ValidateLifetime {
        get;
        set;
    } = true;
}
```


UserTokens.cs file

```csharp
namespace WebApplication.Models;
public class UserTokens {
    public string Token {
        get;
        set;
    }
    public string UserName {
        get;
        set;
    }
    public TimeSpan Validaty {
        get;
        set;
    }
    public string RefreshToken {
        get;
        set;
    }
    public Guid Id {
        get;
        set;
    }
    public string EmailId {
        get;
        set;
    }
    public Guid GuidId {
        get;
        set;
    }
    public DateTime ExpiredTime {
        get;
        set;
    }
}
```


Then we have to add some settings in app settings so we can globally change the token generation settings from appsettings.json without changing any LOC(Line of code).

Note: Please don’t forget to change the local URL of the valid issuer and valid audience.

```csharp
"JsonWebTokenKeys": {
    "ValidateIssuerSigningKey": true,
    "IssuerSigningKey": "64A63153-11C1-4919-9133-EFAF99A9B456",
    "ValidateIssuer": true,
    "ValidIssuer": "https://localhost:7168",
    "ValidateAudience": true,
    "ValidAudience": "https://localhost:7168",
    "RequireExpirationTime": true,
    "ValidateLifetime": true
},
```

C#

Copy

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations5.png)

The next step is to add JWT Helper class that is used to create a Token and Refresh Token and validation of Token.

To add class first create “JwtHelpers” folder in the root project then create a class.

Add code given below,

```csharp
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using WebApplication.Models;
namespace WebApplication.JwtHelpers {
    public static class JwtHelpers {
        public static IEnumerable < Claim > GetClaims(this UserTokens userAccounts, Guid Id) {
            IEnumerable < Claim > claims = new Claim[] {
                new Claim("Id", userAccounts.Id.ToString()),
                    new Claim(ClaimTypes.Name, userAccounts.UserName),
                    new Claim(ClaimTypes.Email, userAccounts.EmailId),
                    new Claim(ClaimTypes.NameIdentifier, Id.ToString()),
                    new Claim(ClaimTypes.Expiration, DateTime.UtcNow.AddDays(1).ToString("MMM ddd dd yyyy HH:mm:ss tt"))
            };
            return claims;
        }
        public static IEnumerable < Claim > GetClaims(this UserTokens userAccounts, out Guid Id) {
            Id = Guid.NewGuid();
            return GetClaims(userAccounts, Id);
        }
        public static UserTokens GenTokenkey(UserTokens model, JwtSettings jwtSettings) {
            try {
                var UserToken = new UserTokens();
                if (model == null) throw new ArgumentException(nameof(model));
                // Get secret key
                var key = System.Text.Encoding.ASCII.GetBytes(jwtSettings.IssuerSigningKey);
                Guid Id = Guid.Empty;
                DateTime expireTime = DateTime.UtcNow.AddDays(1);
                UserToken.Validaty = expireTime.TimeOfDay;
                var JWToken = new JwtSecurityToken(issuer: jwtSettings.ValidIssuer, audience: jwtSettings.ValidAudience, claims: GetClaims(model, out Id), notBefore: new DateTimeOffset(DateTime.Now).DateTime, expires: new DateTimeOffset(expireTime).DateTime, signingCredentials: new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256));
                UserToken.Token = new JwtSecurityTokenHandler().WriteToken(JWToken);
                UserToken.UserName = model.UserName;
                UserToken.Id = model.Id;
                UserToken.GuidId = Id;
                return UserToken;
            } catch (Exception) {
                throw;
            }
        }
    }
}
```

Here GetClaims() Method is used to create return claims list from user token details.

```csharp
// Get secret key
var key = System.Text.Encoding.ASCII.GetBytes(jwtSettings.IssuerSigningKey);
Guid Id = Guid.Empty;
DateTime expireTime = DateTime.UtcNow.AddDays(1);
```


Now get byte arrays of specified keys in appsettings and here we define expiry of token as one day from the day when token is generated.

```csharp
var JWToken = new JwtSecurityToken(issuer: jwtSettings.ValidIssuer, audience: jwtSettings.ValidAudience, claims: GetClaims(model, out Id), notBefore: new DateTimeOffset(DateTime.Now).DateTime, expires: new DateTimeOffset(expireTime).DateTime, signingCredentials: new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256));
UserToken.Token = new JwtSecurityTokenHandler().WriteToken(JWToken);
```

Then we assigned generated security token and access token by using JwtSecurityTokenHandler’s WriteToken() method/ function.

Then we have to do some settings in the program file. We need to inject services to use JWT Token.

In a previous version of .net3.1, we have separated startup files where we have to inject services and use them in your project but the .net6 startup file is no longer exists. So, to inject services let's create a New Class named “AddJWTTokenServicesExtensions” to the separation of concern and without messing off the program.cs first create folder named “Extensions” in your root project. Then create class AddJWTTokenServicesExtensions.

**Note**
Here we need to make these classes static classes because we need to call that method in program.cs.

```csharp
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using WebApplication.Models;
namespace WebApplication.Extensions {
    public static class AddJWTTokenServicesExtensions {
        public static void AddJWTTokenServices(IServiceCollection Services, IConfiguration Configuration) {
            // Add Jwt Setings
            var bindJwtSettings = new JwtSettings();
            Configuration.Bind("JsonWebTokenKeys", bindJwtSettings);
            Services.AddSingleton(bindJwtSettings);
            Services.AddAuthentication(options => {
                options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
            }).AddJwtBearer(options => {
                options.RequireHttpsMetadata = false;
                options.SaveToken = true;
                options.TokenValidationParameters = new Microsoft.IdentityModel.Tokens.TokenValidationParameters() {
                    ValidateIssuerSigningKey = bindJwtSettings.ValidateIssuerSigningKey,
                        IssuerSigningKey = new SymmetricSecurityKey(System.Text.Encoding.UTF8.GetBytes(bindJwtSettings.IssuerSigningKey)),
                        ValidateIssuer = bindJwtSettings.ValidateIssuer,
                        ValidIssuer = bindJwtSettings.ValidIssuer,
                        ValidateAudience = bindJwtSettings.ValidateAudience,
                        ValidAudience = bindJwtSettings.ValidAudience,
                        RequireExpirationTime = bindJwtSettings.RequireExpirationTime,
                        ValidateLifetime = bindJwtSettings.RequireExpirationTime,
                        ClockSkew = TimeSpan.FromDays(1),
                };
            });
        }
    }
}
```



 Add above code to your “AddJWTTokenServicesExtensions.cs” file

Then add the need to call this extension method in the program.cs class.

Add using in the first line of the program.cs

*e.g.*

```csharp
using WebApplication.Extensions;
```



After builder object creation call method AddJWTTokenServices()

e.g.

```csharp
using WebApplication.Extensions;
var builder = Microsoft.AspNetCore.Builder.WebApplication.CreateBuilder(args);
// Add services to the container.
builder.Services.AddJWTTokenServices(builder.Configuration);
```


your program. cs file to look like below.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations6.png)

Let's move to the next step that is controller implementations.

Add new WebAPI Controller Named “AccountController”

Here we don’t use any database, we just static values to validate a user and generate Access Token and Authenticate and Authorized Web API Controller

Create add new class Users in models folders

With the following code.

```csharp
namespace WebApplication.Models {
    public class Users {
        public string UserName {
            get;
            set;
        }
        public Guid Id {
            get;
            set;
        }
        public string EmailId {
            get;
            set;
        }
        public string Password {
            get;
            set;
        }
    }
}
```


Create add new class UserLogins in models folders with following code.

```csharp
using System.ComponentModel.DataAnnotations;
namespace WebApplication.Models {
    public class UserLogins {
        [Required]
        public string UserName {
            get;
            set;
        }
        [Required]
        public string Password {
            get;
            set;
        }
        public UserLogins() {}
    }
}
```


Add new Controller -> API In templates and Rights side Select API Controller -> Empty.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations7.png)

Add following code.

```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using WebApplication.Models;
namespace WebApplication.Controllers {
    [Route("api/[controller]/[action]")]
    [ApiController]
    public class AccountController: ControllerBase {
        private readonly JwtSettings jwtSettings;
        public AccountController(JwtSettings jwtSettings) {
            this.jwtSettings = jwtSettings;
        }
        private IEnumerable < Users > logins = new List < Users > () {
            new Users() {
                    Id = Guid.NewGuid(),
                        EmailId = "adminakp@gmail.com",
                        UserName = "Admin",
                        Password = "Admin",
                },
                new Users() {
                    Id = Guid.NewGuid(),
                        EmailId = "adminakp@gmail.com",
                        UserName = "User1",
                        Password = "Admin",
                }
        };
        [HttpPost]
        public IActionResult GetToken(UserLogins userLogins) {
            try {
                var Token = new UserTokens();
                var Valid = logins.Any(x => x.UserName.Equals(userLogins.UserName, StringComparison.OrdinalIgnoreCase));
                if (Valid) {
                    var user = logins.FirstOrDefault(x => x.UserName.Equals(userLogins.UserName, StringComparison.OrdinalIgnoreCase));
                    Token = JwtHelpers.JwtHelpers.GenTokenkey(new UserTokens() {
                        EmailId = user.EmailId,
                            GuidId = Guid.NewGuid(),
                            UserName = user.UserName,
                            Id = user.Id,
                    }, jwtSettings);
                } else {
                    return BadRequest($ "wrong password");
                }
                return Ok(Token);
            } catch (Exception ex) {
                throw;
            }
        }
        /// <summary>
        /// Get List of UserAccounts
        /// </summary>
        /// <returns>List Of UserAccounts</returns>
        [HttpGet]
        [Authorize(AuthenticationSchemes = Microsoft.AspNetCore.Authentication.JwtBearer.JwtBearerDefaults.AuthenticationScheme)]
        public IActionResult GetList() {
            return Ok(logins);
        }
    }
}
```


In the above Account, the controller created a List of Login Details that are valid users. You can use database records to validate user logins. Next, we created a method to validate login credentials and generate tokens with the help of JWT Hepler. 

And to check authorization from swagger replace open program.cs

```csharp
builder.Services.AddSwaggerGen();
```

with following code

```csharp
builder.Services.AddSwaggerGen(options => {
    options.AddSecurityDefinition("Bearer", new Microsoft.OpenApi.Models.OpenApiSecurityScheme {
        Name = "Authorization",
            Type = Microsoft.OpenApi.Models.SecuritySchemeType.Http,
            Scheme = "Bearer",
            BearerFormat = "JWT",
            In = Microsoft.OpenApi.Models.ParameterLocation.Header,
            Description = "JWT Authorization header using the Bearer scheme."
    });
    options.AddSecurityRequirement(new Microsoft.OpenApi.Models.OpenApiSecurityRequirement {
        {
            new Microsoft.OpenApi.Models.OpenApiSecurityScheme {
                    Reference = new Microsoft.OpenApi.Models.OpenApiReference {
                        Type = Microsoft.OpenApi.Models.ReferenceType.SecurityScheme,
                            Id = "Bearer"
                    }
                },
                new string[] {}
        }
    });
});
```

To check web api with swagger we need to add authorization security options in swagger, so used AddSecurityDefination() and AddSecurityRequirement() function to add Security options.

After running the application you will get the result of the swagger just shown below:

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations8.png)

Let’s try to get Token by specifying username and password.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations9.png)

You will get tokens as shown below.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations10.png)

Without passing the token result will be shown below it will give a 401 error.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations11.png)

To Validate or pass the token in the header click on validate button paste generated token in the textbox click on login. And close the popup dialog.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations12.png)

Then try to get a list of accounts you will get all details.

![Jwt Token Authentication and Authorizations in .Net Core 6.0 WEB API](https://f4n3x6c5.stackpathcdn.com/article/jwt-token-authentication-and-authorizations-in-net-core-6-0-web-api/Images/Jwt%20Token%20Authentication%20and%20Authorizations13.png)

## Summary

In this article, I discussed how we can create a JWT access token. We also saw how we can authorize the WEB API endpoint.



 