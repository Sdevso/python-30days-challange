"""
Day 1: Setup & Print - Hello Python DevOps

Objective:
Write your first Python script for DevOps automation! Today you'll set up your
environment and learn the basics of printing output.

Learning Objectives:
1. Setting up Python development environment
2. Understanding print() function
3. Working with strings and formatting
4. Creating readable output

Detailed Instructions:
1. Environment Setup (15 mins):
   - Install Python 3.x from python.org
   - Install VS Code
   - Install Python extension in VS Code
   - Create a new file 'day1_hello_devops.py'

2. Basic Printing (10 mins):
   - Use print() to display messages
   - Try both single and double quotes
   - Print multiple items

3. System Information (15 mins):
   - Import 'platform' module
   - Get Python version
   - Get OS information

4. Format Output (20 mins):
   - Create section headers with dashes
   - Use f-strings for dynamic content
   - Format date/time information

Key Concepts:
1. print() function:
   - Basic: print("Hello")
   - Multiple items: print("Hi", name, "!");
   - With separator: print("Hi", "there", sep="-")

2. String quotes:
   - Single: 'Hello DevOps'
   - Double: "Hello DevOps"
   - Triple: '''Multi-line text'''

3. String formatting:
   - f-strings: f"Hello {name}"
   - Format method: "Hello {}".format(name)

Code Structure Example:
```python
# Simple print examples
print("Hello, DevOps World!")
print('System Status:', 'OK')

# Print with formatting
name = "DevOps Engineer"
print(f"Welcome, {name}")
```

Challenge Tasks:
1. Print Python version and current time
2. Create a formatted system info display
3. Add some decorative lines between sections
4. Use different string formatting methods

Tips for Success:
- Test each print statement separately
- Use descriptive messages
- Add comments to explain your code
- Try both string formatting styles
- Keep output neat and readable

Common Mistakes to Avoid:
- Forgetting parentheses in print()
- Mixing single/double quotes incorrectly
- Not closing string quotes
- Using + when , works better in print()
"""

# Only necessary imports
import platform
import time

# Your code starts here:
# 1. Print Python version information
print("Python Version:", platform.python_version())
# 2. Create welcome messages using different string types
print('Hello, DevOps World!')
print("This is my first Python script.")
# 3. Try basic string concatenation
print("DevOps = " + "Development" + " + " + "Operations")
# 4. Use simple string formatting
name = "DevOps Engineer"
print(f"Welcome, {name}")

# Decorative lines
print("-" * 24)

# System information
print("System Information:")
print("Operating System:", platform.system())
print("Machine:", platform.machine())
print("Processor:", platform.processor())

# Current time
print("Current Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# Tips:
# - Try both single and double quotes
# - Use + to concatenate strings
# - Try different print() arguments
# - Add some horizontal lines for formatting