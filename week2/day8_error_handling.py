"""
Day 8: File Reading - Server Configuration Reader

Objective:
Build a robust server configuration reader that can handle various file formats
and deal with common file operation errors.

Learning Objectives:
1. Reading files in Python
2. Handling file errors
3. Processing file content
4. Working with file paths

Detailed Instructions:
1. File Reading Basics (15 mins):
   - Open files safely
   - Read file content
   - Process text data
   - Close file handles

2. Error Handling (15 mins):
   - Handle missing files
   - Deal with permissions
   - Manage encoding issues
   - Handle IO errors

3. Content Processing (15 mins):
   - Read line by line
   - Parse file content
   - Extract information
   - Format data

4. Advanced Techniques (15 mins):
   - Read large files
   - Handle different formats
   - Process in chunks
   - Memory management

Key Concepts:
1. File Operations:
   ```python
   # Basic file reading
   with open('config.txt', 'r') as file:
       content = file.read()
   
   # Reading lines
   with open('servers.txt') as file:
       for line in file:
           process_line(line.strip())
   ```

2. Error Handling:
   ```python
   try:
       with open('config.txt') as f:
           data = f.read()
   except FileNotFoundError:
       print("Config file missing")
   ```

Challenge Tasks:
1. Read multiple formats
2. Add error recovery
3. Process large files
4. Create file summaries

Tips for Success:
- Always use with statements
- Check file existence
- Handle all errors
- Close files properly

Common Mistakes to Avoid:
- Not closing files
- Missing error handling
- Memory overflow
- Encoding issues
"""

# Only necessary imports
import os
from typing import Dict, List, Optional

class ServerNotFoundError(Exception):
    """Custom exception for when a server is not found in inventory"""
    pass

class ServiceNotRunningError(Exception):
    """Custom exception for when a required service is not running"""
    pass

def check_server_status(server_name):
    # TODO: Implement server status check with proper error handling
    pass

def read_server_config(file_path: str, encoding: str = 'utf-8') -> List[Dict[str, str]]:
    """
    Read server configuration from a file.

    Args:
        file_path (str): Path to the server configuration file.
        encoding (str): Encoding of the file. Defaults to 'utf-8'.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing server information.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        PermissionError: If there is a permission issue accessing the file.
        UnicodeDecodeError: If there is an encoding problem while reading the file.
        Exception: For any other unexpected errors.
    """
    server_list = []
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            for line in file:
                try:
                    # Assuming each line is a new server in the format: name:ip:port
                    name, ip, port = line.strip().split(':')
                    server_list.append({'name': name, 'ip': ip, 'port': port})
                except ValueError:
                    print(f"Skipping line due to formatting issue: {line.strip()}")
    except FileNotFoundError:
        print(f"Configuration file not found: {file_path}")
    except PermissionError:
        print(f"Permission denied while accessing the file: {file_path}")
    except UnicodeDecodeError:
        print(f"Encoding error while reading the file: {file_path}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    return server_list

def main():
    try:
        # TODO: Implement main function with error handling
        pass
    except ServerNotFoundError as e:
        print(f"Error: {e}")
    except ServiceNotRunningError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    servers = read_server_config('servers.txt')
    for server in servers:
        print(f"Found server - Name: {server['name']}, IP: {server['ip']}, Port: {server['port']}")
    
    main()
