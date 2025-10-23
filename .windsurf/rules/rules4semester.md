---
trigger: always_on
description: 
globs: 
---

# PyCharm Code Style & Project Rules
## 4th Semester Engineering - Clean & Essential Python

## Code Inspection Settings

### 1. Simplicity & Readability
- **Enable**: PEP 8 naming conventions
- **Enable**: Line length warning (max 100 characters)
- **Enable**: Missing docstrings for classes and functions
- **Disable**: Lambda can be replaced with function
- **Disable**: List/Dict comprehension can be converted
- **Enable**: Function is too complex (cyclomatic complexity > 10)
- **Enable**: Too many local variables (> 10)

### 2. Naming Conventions (English Only)
```python
# Variables and functions: camelCase
userName = "John"
def calculateTotal(): pass

# Classes: PascalCase
class UserController: pass
class OrderModel: pass

# Constants: UPPER_SNAKE_CASE
MAX_CONNECTIONS = 100
API_VERSION = "1.0"

# Files: lowercase_with_underscores
user_controller.py
order_service.py
```

### 3. Forbidden Patterns (Intermediate Level)
- ❌ Lambda functions (use regular functions)
- ❌ List/dict comprehensions (use explicit loops)
- ❌ Decorators (except @property, @staticmethod, @classmethod)
- ❌ Generators and yield
- ❌ Context managers (with custom __enter__/__exit__)
- ❌ Metaclasses
- ❌ async/await (unless strictly necessary for FastAPI)
- ❌ * and ** unpacking in function calls
- ❌ Walrus operator (:=)

### 4. Allowed OOP Concepts
- ✅ Classes and objects
- ✅ Inheritance (simple hierarchy, max 2-3 levels)
- ✅ Encapsulation (private attributes with _)
- ✅ Polymorphism (method overriding)
- ✅ Abstract classes (ABC)
- ✅ Properties (@property)
- ✅ Static methods (@staticmethod)
- ✅ Class methods (@classmethod)

### 5. Project Structure
```
project_root/
├── main.py                 # FastAPI entry point
├── requirements.txt
├── .env
├── README.md
│
├── app/
│   ├── __init__.py
│   ├── controllers/        # Business logic
│   │   ├── __init__.py
│   │   └── user_controller.py
│   │
│   ├── models/            # Data entities
│   │   ├── __init__.py
│   │   └── user_model.py
│   │
│   ├── views/             # FastAPI endpoints
│   │   ├── __init__.py
│   │   └── user_routes.py
│   │
│   ├── services/          # Shared logic
│   │   ├── __init__.py
│   │   └── validation_service.py
│   │
│   └── utils/             # Helpers
│       ├── __init__.py
│       └── date_utils.py
│
└── tests/
    ├── __init__.py
    └── test_user_controller.py
```

## PyCharm Configuration Steps

### File Templates
**Settings → Editor → File and Code Templates**

**Python Class Template:**
```python
"""
Module: ${NAME}
Description: [Brief description]
Author: [Your name]
Date: ${DATE}
"""


class ${NAME}:
    """
    [Class description]
    """
    
    def __init__(self):
        """Initialize ${NAME}"""
        pass
```

**Python Script Template:**
```python
"""
Module: ${NAME}
Description: [Brief description]
Author: [Your name]
Date: ${DATE}
"""


def main():
    """Main function"""
    pass


if __name__ == "__main__":
    main()
```

### Code Style Settings
**Settings → Editor → Code Style → Python**

- **Tabs and Indents**: 4 spaces
- **Wrapping and Braces**: 100 max line length
- **Blank Lines**: 
  - Around class: 2
  - Around method: 1
  - Around top-level: 2

### Inspections Profile
**Settings → Editor → Inspections → Python**

Enable:
- ✅ PEP 8 naming convention violation
- ✅ Function has too many local variables
- ✅ Overly complex function
- ✅ Missing type hinting
- ✅ Shadowing names from outer scopes
- ✅ Unused local variable
- ✅ Statement has no effect

Disable:
- ❌ Lambda can be replaced with function
- ❌ Can be replaced with comprehension
- ❌ Simplify boolean expression

### Live Templates (Code Snippets)

**Settings → Editor → Live Templates → Python**

**`cls` - Basic Class:**
```python
class $CLASS_NAME$:
    """$DESCRIPTION$"""
    
    def __init__(self):
        """Initialize $CLASS_NAME$"""
        $END$
```

**`def` - Function with docstring:**
```python
def $NAME$($PARAMS$):
    """
    $DESCRIPTION$
    
    Args:
        $ARGS$
    
    Returns:
        $RETURN$
    """
    $END$
```

**`for` - Simple for loop:**
```python
for $VAR$ in $ITERABLE$:
    $END$
```

**`if` - Simple if statement:**
```python
if $CONDITION$:
    $END$
```

## Code Example (Approved Style)
```python
"""
Module: user_controller
Description: Handles user business logic
Author: Student Name
Date: 2025-10-23
"""

from app.models.user_model import UserModel
from app.services.validation_service import ValidationService


class UserController:
    """
    Controller for managing user operations
    """
    
    def __init__(self):
        """Initialize UserController"""
        self._validationService = ValidationService()
        self._users = []
    
    def createUser(self, userName: str, userEmail: str) -> UserModel:
        """
        Creates a new user after validation
        
        Args:
            userName: The user's name
            userEmail: The user's email
            
        Returns:
            UserModel: The created user
            
        Raises:
            ValueError: If validation fails
        """
        # Validate input
        if not self._validationService.isValidEmail(userEmail):
            raise ValueError("Invalid email format")
        
        # Create user
        newUser = UserModel()
        newUser.name = userName
        newUser.email = userEmail
        
        # Store user
        self._users.append(newUser)
        
        return newUser
    
    def getAllUsers(self) -> list:
        """
        Returns all users
        
        Returns:
            list: List of UserModel objects
        """
        return self._users
```

## Quick Checklist Before Committing

- [ ] All variables and functions in camelCase
- [ ] All classes in PascalCase
- [ ] All files in lowercase_with_underscores
- [ ] No lambda functions used
- [ ] No list/dict comprehensions
- [ ] Docstrings for all classes and functions
- [ ] Type hints for function parameters
- [ ] No lines longer than 100 characters
- [ ] English names only
- [ ] Comments explain "why", not "what"
- [ ] Each function does ONE thing
- [ ] No nested functions deeper than 3 levels

## Essential Dependencies Only
```txt
# requirements.txt
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
python-dotenv==1.0.0
```

## Running the Project
```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload

# Run tests
pytest tests/
```

---
**Remember**: Write code that your future self can understand in 6 months. Clarity > Cleverness.