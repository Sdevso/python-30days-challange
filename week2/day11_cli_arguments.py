"""
Day 11: Exceptions - Robust Error Handler

Objective:
Build a robust error handling system for file operations and server
management tasks, focusing on graceful error recovery and user feedback.

Learning Objectives:
1. Understanding try/except blocks
2. Handling specific exceptions
3. Implementing error recovery
4. Creating custom exceptions

Detailed Instructions:
1. Basic Error Handling (15 mins):
   - Write try/except blocks
   - Catch specific exceptions
   - Handle file errors
   - Provide error messages

2. Custom Exceptions (15 mins):
   - Create exception classes
   - Add custom messages
   - Include error details
   - Handle multiple errors

3. Error Recovery (15 mins):
   - Implement retry logic
   - Add fallback options
   - Create recovery steps
   - Log error details

4. Advanced Features (15 mins):
   - Chain exception handling
   - Use context managers
   - Add cleanup code
   - Create error reports

Key Concepts:
1. Exception Handling:
   ```python
   try:
       with open('config.txt') as f:
           data = f.read()
   except FileNotFoundError:
       print('Config file missing')
   except PermissionError:
       print('Access denied')
   finally:
       print('Cleanup code')
   ```

2. Custom Exceptions:
   ```python
   class ServerError(Exception):
       def __init__(self, server, message):
           self.server = server
           self.message = message
           super().__init__(f"{server}: {message}")
   ```

Challenge Tasks:
1. Add retry mechanism
2. Create error logging
3. Implement recovery
4. Add error reporting

Tips for Success:
- Be specific with exceptions
- Always clean up resources
- Log error details
- Plan recovery steps

Common Mistakes to Avoid:
- Catching all exceptions
- Empty except blocks
- Missing cleanup code
- Hiding error details
"""

# Only necessary imports
import os
from typing import Dict, List, Optional
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Server Monitoring CLI Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # TODO: Add command line arguments
    
    return parser.parse_args()

def validate_args(args):
    # TODO: Implement argument validation
    pass

def main():
    args = parse_arguments()
    validate_args(args)
    
    # TODO: Implement main functionality using args
    
if __name__ == "__main__":
    main()
