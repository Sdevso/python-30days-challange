"""
Day 28: Logging - Advanced Logger

Objective:
Replace print statements with a proper logging system that can handle
different log levels, formats, and outputs effectively.

Learning Objectives:
1. Using logging module
2. Setting log levels
3. Formatting output
4. Managing handlers

Detailed Instructions:
1. Logger Setup (15 mins):
   - Import logging
   - Configure levels
   - Set formats
   - Add handlers

2. Log Management (15 mins):
   - Create loggers
   - Handle rotation
   - Set retention
   - Manage files

3. Log Formats (15 mins):
   - Add timestamps
   - Include context
   - Format messages
   - Add colors

4. Advanced Features (15 mins):
   - Multiple handlers
   - Custom formatters
   - Filter messages
   - Handle errors

Key Concepts:
1. Basic Setup:
   ```python
   import logging
   
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       filename='app.log'
   )
   ```

2. Custom Logger:
   ```python
   logger = logging.getLogger(__name__)
   handler = logging.FileHandler('app.log')
   formatter = logging.Formatter(
       '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )
   handler.setFormatter(formatter)
   logger.addHandler(handler)
   ```

Challenge Tasks:
1. Add log rotation
2. Create custom formats
3. Implement filters
4. Add error emails

Tips for Success:
- Use proper levels
- Add good context
- Rotate log files
- Handle errors

Common Mistakes to Avoid:
- Using print()
- Missing context
- No rotation
- Poor formatting
"""

# Only necessary imports
import logging
from logging.handlers import RotatingFileHandler
import os
from typing import Optional

class AdvancedLogger:
    def __init__(self, name: str, log_file: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=10)
        
        # Set level for handlers
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(level)
        
        # Create formatters and add to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        
        # Add handlers to the logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)
    
    def debug(self, msg: str):
        self.logger.debug(msg)
    
    def info(self, msg: str):
        self.logger.info(msg)
    
    def warning(self, msg: str):
        self.logger.warning(msg)
    
    def error(self, msg: str):
        self.logger.error(msg)
    
    def critical(self, msg: str):
        self.logger.critical(msg)

def main():
    # Example usage
    log = AdvancedLogger(__name__, 'app.log')
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')

if __name__ == "__main__":
    main()
