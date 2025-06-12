"""
Day 10: CLI Arguments - Config Manager

Objective:
Build a configuration management system that can handle command-line arguments,
read config files, and manage application settings.

Learning Objectives:
1. Working with sys.argv
2. Parsing command line args
3. Reading config files
4. Managing app settings

Detailed Instructions:
1. Command Line Args (15 mins):
   - Access sys.argv
   - Parse arguments
   - Handle options
   - Set defaults

2. Config File Handling (15 mins):
   - Read config files
   - Parse different formats
   - Validate settings
   - Handle errors

3. Settings Management (15 mins):
   - Combine sources
   - Override settings
   - Validate values
   - Apply defaults

4. Advanced Features (15 mins):
   - Environment variables
   - Multiple formats
   - Config validation
   - Error handling

Key Concepts:
1. Argument Parsing:
   ```python
   # Basic argument handling
   import sys
   
   if len(sys.argv) > 1:
       config_file = sys.argv[1]
   else:
       config_file = 'default.conf'
   ```

2. Config Reading:
   ```python
   # Read config file
   def read_config(filename):
       with open(filename) as f:
           return f.read()
   ```

Challenge Tasks:
1. Support multiple formats
2. Add validation rules
3. Implement config merge
4. Create config wizard

Tips for Success:
- Validate all inputs
- Provide defaults
- Handle missing files
- Document options

Common Mistakes to Avoid:
- Hard-coded paths
- Missing validation
- No error handling
- Unclear help text
"""

# Only necessary imports
import sys
import os
from typing import Dict, List, Optional

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = {}
    
    def load_ini_config(self):
        # TODO: Implement INI config loading
        pass
    
    def load_yaml_config(self):
        # TODO: Implement YAML config loading
        pass
    
    def validate_config(self):
        # TODO: Implement config validation
        pass
    
    def get_server_config(self, server_name: str) -> Optional[Dict]:
        # TODO: Implement server config retrieval
        pass

def main():
    # TODO: Implement main function to demonstrate config management
    pass

if __name__ == "__main__":
    main()
