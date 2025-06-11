"""
Day 4: Server Health Checker

Challenge Description:
Write a script that checks the health status of servers by monitoring various metrics such as:
- CPU usage
- Memory utilization
- Disk space
- Network connectivity
- Running services

Learning Objectives:
1. Work with system metrics
2. Implement health check functions
3. Create a scoring system for server health
4. Handle different types of metrics
5. Implement threshold-based alerts

Requirements:
1. Read server details from Inventory.json
2. Check multiple health metrics for each server
3. Calculate an overall health score (0-100%)
4. Generate alerts for servers below threshold
5. Format output in an easily readable way

Hints:
1. Use psutil library for system metrics:
   - psutil.cpu_percent() for CPU usage
   - psutil.virtual_memory() for memory
   - psutil.disk_usage() for disk space

2. For network connectivity:
   - Use ping or socket connection tests
   - Set appropriate timeouts
   - Handle connection errors

3. Health Score Calculation:
   - Weight different metrics appropriately
   - CPU: 30%
   - Memory: 25%
   - Disk: 25%
   - Network: 20%

4. Alert Thresholds:
   - Critical: < 50%
   - Warning: < 70%
   - Healthy: >= 70%

5. Error Handling:
   - Handle unreachable servers
   - Handle missing metrics
   - Provide meaningful error messages

Bonus Challenges:
1. Add historical tracking of health scores
2. Implement trend analysis
3. Create a simple report generation function
4. Add email notifications for critical status

Tips:
- Use dictionaries to store health metrics
- Implement modular functions for each check
- Add proper error handling
- Use color coding for different status levels
- Add logging for health check results
"""

# Implement your solution here