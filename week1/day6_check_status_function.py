"""
Day 6: Functions - Status Check Module

Objective:
Transform your status checking code into reusable functions, making your code
more organized and maintainable.

Learning Objectives:
1. Understanding function definition and calls
2. Working with parameters and returns
3. Using docstrings and type hints
4. Creating modular code

Detailed Instructions:
1. Basic Functions (15 mins):
   - Create simple function definitions
   - Add parameters
   - Write return statements
   - Call your functions

2. Function Documentation (15 mins):
   - Write clear docstrings
   - Add parameter descriptions
   - Document return values
   - Include usage examples

3. Advanced Parameters (15 mins):
   - Use default values
   - Add optional parameters
   - Handle multiple arguments
   - Use keyword arguments

4. Return Values (15 mins):
   - Return single values
   - Return multiple values
   - Use different return types
   - Handle no return (None)

Key Concepts:
1. Function Basics:
   ```python
   def check_status(server_name: str) -> bool:
       '''Check if server is responding.
       
       Args:
           server_name: Name of server to check
           
       Returns:
           bool: True if server is up
       '''
       # Function logic here
       return True
   ```

2. Parameter Types:
   - Required parameters
   - Optional parameters
   - Default values
   - *args and **kwargs

Challenge Tasks:
1. Create a function library
2. Add error handling
3. Implement logging
4. Create nested functions

Tips for Success:
- Use descriptive function names
- Keep functions focused
- Document all functions
- Test with various inputs

Common Mistakes to Avoid:
- Too many parameters
- Missing documentation
- Unclear return values
- Side effects in functions
"""

# Only necessary imports
from typing import Dict, List, Optional, Tuple

# Implement your solution here
def check_status(server_name: str) -> bool:
    """Check if server is responding.
    
    Args:
        server_name: Name of server to check
        
    Returns:
        bool: True if server is up
    """
    # Function logic here
    return True

def get_service_status(service_name: str) -> str:
    """Get the status of a service.
    
    Args:
        service_name: Name of the service
        
    Returns:
        str: Service status (running/stopped)
    """
    status = "running"  # Check logic here
    return status

# Function with multiple parameters
def monitor_resource(resource_name: str, warning: int = 80, critical: int = 90) -> Dict:
    """Monitor resource usage.
    
    Args:
        resource_name: Name of resource to monitor
        warning: Warning threshold (default: 80)
        critical: Critical threshold (default: 90)
    
    Returns:
        dict: Resource status information
    """
    return {
        "name": resource_name,
        "usage": 75,
        "status": "OK"
    }