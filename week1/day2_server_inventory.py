"""
Day 2: Variables & Data Types - Server Inventory Manager

Objective:
Create a server inventory system using different Python data types to store
and manage server information effectively.

Learning Objectives:
1. Understanding Python variables
2. Working with basic data types
3. Using lists and dictionaries
4. Type conversion and checking

Detailed Instructions:
1. Basic Server Variables (15 mins):
   - Create variables for server name, IP, status
   - Use appropriate data types for each
   - Print and verify variable types

2. Server Lists (15 mins):
   - Create a list of server names
   - Add server IPs to a separate list
   - Combine related information

3. Server Dictionary (15 mins):
   - Create a dictionary for server details
   - Add multiple properties
   - Access dictionary values

4. Data Type Operations (15 mins):
   - Convert strings to integers
   - Join lists and strings
   - Update dictionary values

Key Concepts:
1. Variable Types:
   - str: server names, IPs
   - int: ports, counts
   - bool: status flags
   - list: collections
   - dict: key-value pairs

2. Type Operations:
   - type(): check variable type
   - int(): convert to integer
   - str(): convert to string
   - list(): create/convert to list

Example Structure:
```python
# Basic variables
server_name = "web-server-01"
server_port = 443
is_active = True

# List example
servers = ["web-01", "web-02"]
ports = [80, 443]

# Dictionary example
server_info = {
    "name": "web-01",
    "ip": "192.168.1.100",
    "active": True
}
```

Challenge Tasks:
1. Create a multi-server inventory
2. Add nested dictionaries
3. Implement type validation
4. Create a server status display

Tips for Success:
- Use meaningful variable names
- Keep track of data types
- Test dictionary access
- Validate data before storing

Common Mistakes to Avoid:
- Using wrong data types
- Forgetting dictionary keys
- Not handling missing values
- Mixing data type operations
"""

# Only necessary imports
import json
import os

# Your code starts here:
# 1. Create variables for a server
# 2. Use appropriate data types
# 3. Create a list of servers
# 4. Print server information

# Example structure:
'''
# String variables
server_name = "web-prod-01"
server_ip = "192.168.1.10"

# Integer variables
server_port = 443
max_connections = 1000

# Boolean variables
is_running = True
is_primary = False

# List of servers
server_list = ["web-01", "web-02", "db-01"]

# Dictionary for server metadata
server_info = {
    "name": server_name,
    "port": server_port,
    "status": is_running
}
'''

# Tips:
# - Use meaningful variable names
# - Try different data types
# - Create a small server inventory
# - Print and check variable types