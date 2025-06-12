"""
Day 5: Loops - Service Monitor

Objective:
Build a service monitoring system using loops to continuously check multiple
services and their status.

Learning Objectives:
1. Understanding for loops
2. Working with while loops
3. Using loop control statements
4. Implementing monitoring cycles

Detailed Instructions:
1. For Loop Basics (15 mins):
   - Iterate through service lists
   - Access list elements
   - Use range() function

2. While Loop Usage (15 mins):
   - Create monitoring loops
   - Set exit conditions
   - Handle infinite loops

3. Loop Control (15 mins):
   - Use break statement
   - Use continue statement
   - Implement counters

4. Nested Loops (15 mins):
   - Check multiple servers
   - Monitor multiple services
   - Control nested execution

Key Concepts:
1. For Loop:
   - Basic: for item in list:
   - With range: for i in range(5):
   - With enumerate: for i, item in enumerate(list):

2. While Loop:
   - Basic: while condition:
   - With counter
   - With boolean flag

Example Structure:
```python
# Simple for loop
services = ["web", "db", "cache"]
for service in services:
    print(f"Checking {service}")

# Basic while loop
attempts = 0
while attempts < 3:
    # check service
    attempts += 1
```

Challenge Tasks:
1. Monitor multiple services
2. Add retry logic
3. Implement interval checks
4. Create service dependencies

Tips for Success:
- Always have an exit condition
- Use clear loop variables
- Add progress messages
- Handle loop termination

Common Mistakes to Avoid:
- Infinite loops
- Missing counter updates
- Complex nested loops
- Forgetting break conditions
"""

# Only necessary imports