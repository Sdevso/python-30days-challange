"""
Day 29: Templating - Config Generator

Objective:
Create a template-based configuration generator using Jinja2 to dynamically
generate configuration files for various services and environments.

Learning Objectives:
1. Using Jinja2 templates
2. Managing template files
3. Handling variables
4. Generating configs

Detailed Instructions:
1. Template Basics (15 mins):
   - Install Jinja2
   - Create templates
   - Add variables
   - Use filters

2. Config Structure (15 mins):
   - Define layouts
   - Add sections
   - Include defaults
   - Handle formats

3. Dynamic Content (15 mins):
   - Use conditions
   - Add loops
   - Include macros
   - Handle inheritance

4. Advanced Features (15 mins):
   - Custom filters
   - Error handling
   - Multi-format
   - Validation

Key Concepts:
1. Basic Template:
   ```python
   from jinja2 import Template
   
   template_str = '''
   server {
       listen {{ port }};
       server_name {{ domain }};
       
       location / {
           proxy_pass {{ backend }};
       }
   }
   '''
   
   template = Template(template_str)
   ```

2. Template Rendering:
   ```python
   # Render with variables
   config = template.render(
       port=8080,
       domain='example.com',
       backend='http://localhost:5000'
   )
   ```

Challenge Tasks:
1. Add template inheritance
2. Create custom filters
3. Add validation rules
4. Support multiple formats

Tips for Success:
- Use proper escaping
- Add error handling
- Validate output
- Keep templates clean

Common Mistakes to Avoid:
- Missing escaping
- No validation
- Complex templates
- Hard-coded values
"""

# Only necessary imports
from jinja2 import Template, Environment, FileSystemLoader
from typing import Dict, Any, Optional

class ConfigGenerator:
    def __init__(self, template_dir: str):
        self.env = Environment(loader=FileSystemLoader(template_dir))
    
    def render_template(
        self,
        template_name: str,
        context: Dict[str, Any],
        output_format: Optional[str] = None
    ) -> str:
        template = self.env.get_template(template_name)
        rendered = template.render(context)
        
        if output_format == 'json':
            return json.dumps(rendered)
        elif output_format == 'yaml':
            return yaml.dump(rendered)
        else:
            return rendered

def main():
    # TODO: Implement main function to demonstrate config generator
    pass

if __name__ == "__main__":
    main()
