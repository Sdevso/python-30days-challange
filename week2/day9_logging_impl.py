"""
Day 9: Logging Implementation

Challenge Description:
Implement a comprehensive logging system for your server monitoring application
that captures all important events, errors, and metrics with appropriate detail
levels and formats.

Learning Objectives:
1. Configure logging system
2. Implement different log levels
3. Create custom log formats
4. Handle log rotation

Requirements:
1. Set up logging with:
   - Multiple output handlers
   - Different log levels
   - Custom formatters
   - Log rotation

2. Implement logging for:
   - Application events
   - Server status changes
   - Error conditions
   - Performance metrics

Hints:
1. Log Levels Usage:
   - DEBUG: Detailed debugging info
   - INFO: General operational events
   - WARNING: Minor issues or warnings
   - ERROR: Serious problems
   - CRITICAL: System-wide failures

2. Handler Types:
   - FileHandler: Log to files
   - StreamHandler: Console output
   - RotatingFileHandler: Size-based rotation
   - TimedRotatingFileHandler: Time-based rotation

3. Log Format Example:
   %(asctime)s - %(name)s - %(levelname)s - %(message)s
   Additional fields:
   - %(pathname)s: Full pathname
   - %(filename)s: Filename
   - %(funcName)s: Function name
   - %(lineno)d: Line number

4. Configuration Structure:
   {
       'version': 1,
       'handlers': {
           'file': {
               'class': 'logging.FileHandler',
               'filename': 'app.log',
               'formatter': 'detailed'
           }
       },
       'formatters': {
           'detailed': {
               'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
           }
       }
   }

Bonus Challenges:
1. Add JSON log formatting
2. Implement log aggregation
3. Create log analysis tools
4. Add metrics collection

Tips:
- Use logging.getLogger(__name__)
- Implement log rotation
- Add context information
- Consider log aggregation
- Include error tracebacks
"""

import logging
from logging.handlers import RotatingFileHandler
import os

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
