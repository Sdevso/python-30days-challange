"""
Day 3: Input & F-strings - Interactive Server Query

Objective:
Build an interactive server query tool that takes user input and displays
formatted server information using Python's input() function and f-strings.

Learning Objectives:
1. Using input() for user interaction
2. Mastering f-string formatting
3. Processing user input
4. Creating formatted output

Detailed Instructions:
1. User Input Basics (15 mins):
   - Get server name from user
   - Process different input types
   - Handle empty input

2. F-string Usage (15 mins):
   - Basic f-string syntax
   - Embedding expressions
   - Formatting options

3. Input Processing (15 mins):
   - Split comma-separated input
   - Remove whitespace
   - Convert input types

4. Output Formatting (15 mins):
   - Create status display
   - Format numbers and text
   - Add visual elements

Key Concepts:
1. Input Function:
   - Basic: name = input("Enter name: ")
   - With prompt
   - Input validation

2. F-string Features:
   - Basic: f"Server: {name}"
   - Expressions: f"Memory: {ram * 2}GB"
   - Formatting: f"Usage: {cpu:.2f}%"

Example Structure:
```python
# Basic input
server = input("Enter server name: ")

# Input processing
servers = input("Enter servers (comma-separated): ")
server_list = [s.strip() for s in servers.split(',')]

# F-string formatting
status = "online"
uptime = 98.5
print(f"Server {server} is {status} ({uptime:.1f}% uptime)")
```

Challenge Tasks:
1. Create a multi-server query system
2. Add input validation
3. Format output as a table
4. Implement search functionality

Tips for Success:
- Always validate user input
- Use clear input prompts
- Format output for readability
- Handle edge cases

Common Mistakes to Avoid:
- Not handling invalid input
- Forgetting to strip whitespace
- Complex f-string expressions
- Missing input validation
"""

# Only necessary imports
import json
import os

# Your code starts here:
# 1. Get server details using input()
# 2. Format the input using f-strings
# 3. Create nicely formatted output
# 4. Handle different input types

# Example structure:
'''
# Basic input with f-string
name = input("Enter server name: ")
print(f"Checking server: {name}")

# Multiple inputs formatted together
host = input("Enter host: ")
port = input("Enter port: ")
print(f"Server address: {host}:{port}")

# F-string with expressions
memory = input("Enter memory (GB): ")
print(f"Memory available: {int(memory) * 1024}MB")

# Multi-line f-string output
status = input("Enter status (up/down): ")
output = f"""
Server Status Report
-------------------
Name: {name}
Address: {host}:{port}
Status: {status.upper()}
Memory: {memory}GB
-------------------
"""
print(output)
'''

# Tips:
# - Use descriptive input prompts
# - Format output for readability
# - Try nested f-strings
# - Use f-strings with different data types
