"""
Day 7: Modules - File System Operations

Objective:
Create a file system checker module using Python's built-in modules to monitor
and manage system files and directories.

Learning Objectives:
1. Understanding Python modules
2. Using os and sys modules
3. Working with file paths
4. Creating custom modules

Detailed Instructions:
1. Module Basics (15 mins):
   - Import built-in modules
   - Access module functions
   - Understand module scope
   - Create module variables

2. File Operations (15 mins):
   - Check file existence
   - Get file information
   - Handle file paths
   - Work with directories

3. Custom Module (15 mins):
   - Create module structure
   - Add module functions
   - Write documentation
   - Test functionality

4. Module Integration (15 mins):
   - Import custom modules
   - Use module functions
   - Handle module errors
   - Create module tests

Key Concepts:
1. Module Import Methods:
   ```python
   # Different import styles
   import os
   from os import path
   from os.path import exists as file_exists
   ```

2. Common Module Functions:
   ```python
   # File operations
   os.path.exists(file_path)
   os.path.getsize(file_path)
   os.listdir(directory)
   ```

Challenge Tasks:
1. Create a file monitor
2. Add file statistics
3. Implement file search
4. Create backup utility

Tips for Success:
- Use absolute paths
- Handle path separators
- Check file permissions
- Close file handles

Common Mistakes to Avoid:
- Hardcoded paths
- Missing error handling
- Platform-specific code
- Resource leaks
"""

# Only necessary imports
import os
import sys
from typing import Dict, List, Optional

# Module-level variables
DEFAULT_PATH = "."
IGNORE_PATTERNS = [".git", "__pycache__", "*.pyc"]

def check_file_exists(filename: str) -> bool:
    """Check if a file exists.
    
    Args:
        filename: Name of file to check
        
    Returns:
        bool: True if file exists
    """
    return os.path.exists(filename)

def get_file_info(filepath: str) -> Dict:
    """Get file information.
    
    Args:
        filepath: Path to the file
        
    Returns:
        dict: File information
    """
    return {
        "size": os.path.getsize(filepath),
        "modified": time.ctime(os.path.getmtime(filepath)),
        "type": "file" if os.path.isfile(filepath) else "directory"
    }

# If run as a script
if __name__ == "__main__":
    # Test the module
    print(check_file_exists("test.txt"))