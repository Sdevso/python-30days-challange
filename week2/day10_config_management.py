"""
Day 10: Configuration Management

Challenge Description:
Create a flexible configuration management system that can handle multiple
config formats, validate settings, and provide easy access to configuration
values throughout your application.

Learning Objectives:
1. Handle multiple config formats
2. Implement config validation
3. Manage default values
4. Create config inheritance

Requirements:
1. Support multiple formats:
   - YAML
   - JSON
   - INI
   - ENV variables

2. Implement features:
   - Config validation
   - Default values
   - Environment overrides
   - Config inheritance

Hints:
1. Config File Structure:
   yaml_example:
     app:
       name: ServerMonitor
       version: 1.0
     monitoring:
       interval: 300
       timeout: 30
     servers:
       - name: prod-1
         ip: 10.0.0.1
         services:
           - nginx
           - mysql

2. Validation Rules:
   - Required fields
   - Data types
   - Value ranges
   - Format patterns
   - Dependencies

3. Environment Handling:
   - Load order:
     1. Default config
     2. Config files
     3. Environment variables
     4. Command line args

4. Config Access Methods:
   - Dot notation
   - Dictionary style
   - Environment variables
   - Default values

Bonus Challenges:
1. Add schema validation
2. Implement config versioning
3. Add secure credential handling
4. Create config documentation

Tips:
- Use strong typing
- Implement config caching
- Add change detection
- Support hot reloading
- Include config documentation
"""

import configparser
import yaml
import os

class ConfigManager:
    def __init__(self, config_path):
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
    
    def get_server_config(self, server_name):
        # TODO: Implement server config retrieval
        pass

def main():
    # TODO: Implement main function to demonstrate config management
    pass

if __name__ == "__main__":
    main()
