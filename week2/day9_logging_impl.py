"""
Day 9: File Writing - Log File Manager

Objective:
Create a logging system that can write and append server status information
to log files, with proper formatting and organization.

Learning Objectives:
1. Understanding file write modes
2. Working with append operations
3. Formatting log entries
4. Managing log files

Detailed Instructions:
1. File Writing Basics (15 mins):
   - Open files in write mode
   - Write basic content
   - Format output
   - Close files properly

2. Append Operations (15 mins):
   - Use append mode
   - Add new entries
   - Maintain file structure
   - Handle existing files

3. Log Formatting (15 mins):
   - Add timestamps
   - Structure log entries
   - Include metadata
   - Format for readability

4. Log Management (15 mins):
   - Implement log rotation
   - Handle large files
   - Manage old logs
   - Add file backup

Key Concepts:
1. File Modes:
   ```python
   # Write mode - creates new file
   with open('app.log', 'w') as f:
       f.write('Log Started\\n')
   
   # Append mode - adds to existing
   with open('app.log', 'a') as f:
       f.write('New Entry\\n')
   ```

2. Log Entry Format:
   ```python
   from datetime import datetime
   
   timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   log_entry = f'[{timestamp}] Server started\\n'
   ```

Challenge Tasks:
1. Create log rotation
2. Add compression
3. Implement cleanup
4. Add log analysis

Tips for Success:
- Always use with blocks
- Add error handling
- Include timestamps
- Structure log entries

Common Mistakes to Avoid:
- Not closing files
- Missing timestamps
- Unstructured logs
- No log rotation
"""

# Only necessary imports
import os
from datetime import datetime
from typing import Dict, List, Optional

import logging
from logging.handlers import RotatingFileHandler

# Setup logging configuration
def setup_logging():
    # TODO: Configure logging with both file and console handlers
    # TODO: Set up log rotation
    # TODO: Configure log format
    pass

def monitor_server(server_name):
    # TODO: Implement server monitoring with proper logging
    pass

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # TODO: Implement main function with logging
        pass
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
