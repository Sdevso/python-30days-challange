"""
Day 4: Conditions - Server Health Logic

Objective:
Implement a server health checking system using conditional statements to
evaluate different metrics and determine server status.

Learning Objectives:
1. Understanding if/elif/else statements
2. Using comparison operators
3. Working with boolean logic
4. Implementing complex conditions

Detailed Instructions:
1. Basic Conditions (15 mins):
   - Write simple if statements
   - Use comparison operators
   - Test boolean conditions

2. Status Levels (15 mins):
   - Implement warning thresholds
   - Add critical thresholds
   - Create status messages

3. Multiple Checks (15 mins):
   - Combine CPU and memory checks
   - Use AND/OR operators
   - Handle multiple conditions

4. Health Score (15 mins):
   - Calculate overall health
   - Weight different metrics
   - Format status output

Key Concepts:
1. Conditional Statements:
   - if condition:
   - elif condition:
   - else:
   
2. Comparison Operators:
   - == (equal)
   - != (not equal)
   - >, <, >=, <= (comparisons)

Example Structure:
```python
# Basic condition
if cpu_usage > 90:
    status = "Critical"

# Multiple conditions
if cpu_usage > 90 and memory_usage > 85:
    status = "Critical"
elif cpu_usage > 70 or memory_usage > 70:
    status = "Warning"
else:
    status = "Normal"
```

Challenge Tasks:
1. Add multiple health metrics
2. Implement status severity levels
3. Create health score calculation
4. Add threshold configuration

Tips for Success:
- Start with simple conditions
- Test each condition separately
- Use clear comparison values
- Add status messages

Common Mistakes to Avoid:
- Complex nested conditions
- Missing edge cases
- Unclear status messages
- Hard-coded values
"""

# Only necessary imports