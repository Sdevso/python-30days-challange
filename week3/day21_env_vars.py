"""
Day 21: Environment Variables - Secure Configuration

Objective:
Create a secure configuration system using environment variables to manage
sensitive data like credentials and API keys.

Learning Objectives:
1. Working with env vars
2. Managing credentials
3. Securing configuration
4. Loading from .env

Detailed Instructions:
1. Environment Setup (15 mins):
   - Access env vars
   - Set variables
   - Use os.environ
   - Handle defaults

2. Secure Loading (15 mins):
   - Load .env files
   - Parse variables
   - Handle secrets
   - Set permissions

3. Configuration (15 mins):
   - Create config class
   - Load from env
   - Set defaults
   - Validate values

4. Security Features (15 mins):
   - Mask secrets
   - Validate input
   - Handle errors
   - Log securely

Key Concepts:
1. Environment Variables:
   ```python
   import os
   from typing import Optional
   
   def get_env(key: str, default: Optional[str] = None) -> str:
       return os.environ.get(key, default)
   ```

2. Secure Config:
   ```python
   from dotenv import load_dotenv
   
   # Load .env file
   load_dotenv()
   
   # Get sensitive data
   db_password = os.getenv('DB_PASSWORD')
   ```

Challenge Tasks:
1. Add encryption
2. Implement rotation
3. Create secure store
4. Add validation

Tips for Success:
- Never commit secrets
- Use .env files
- Set proper permissions
- Validate all input

Common Mistakes to Avoid:
- Hardcoded secrets
- Exposed credentials
- Insecure logging
- Missing validation
"""

# Only necessary imports
import os
from typing import Dict, Optional
from dotenv import load_dotenv

def get_env(key: str, default: Optional[str] = None) -> str:
    """Gets an environment variable or returns the default value."""
    return os.environ.get(key, default)

# Load .env file
load_dotenv()

# Example of getting a sensitive variable
db_password = get_env('DB_PASSWORD')
