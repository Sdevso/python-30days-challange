"""
Day 11: Command Line Arguments

Challenge Description:
Create a comprehensive command-line interface for your server monitoring
application that provides intuitive commands, options, and help documentation.

Learning Objectives:
1. Design CLI interfaces
2. Implement argument parsing
3. Create help documentation
4. Handle user input

Requirements:
1. Implement commands for:
   - Server status checks
   - Service management
   - Configuration updates
   - Report generation

2. Support features:
   - Subcommands
   - Required/optional args
   - Default values
   - Help text

Hints:
1. Command Structure:
   servermon <command> [options]
   
   Commands:
   - status: Check server status
   - service: Manage services
   - config: Update configuration
   - report: Generate reports

2. Options Example:
   servermon status --server web-01 --service nginx --format json
   
   Common Options:
   --server: Target server
   --service: Target service
   --format: Output format
   --verbose: Detail level

3. Argument Groups:
   - Main commands
   - Server selection
   - Output formatting
   - Authentication
   - Logging options

4. Help Documentation:
   - Command overview
   - Option descriptions
   - Usage examples
   - Error messages

Bonus Challenges:
1. Add command completion
2. Implement interactive mode
3. Create config wizard
4. Add batch processing

Tips:
- Use argparse subcommands
- Add detailed help text
- Implement input validation
- Include usage examples
- Handle errors gracefully
"""

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
