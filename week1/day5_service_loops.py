"""
Day 5: Service Monitor

Challenge Description:
Create a script that monitors multiple services running on different servers.
The script should check service status, uptime, and resource usage.

Learning Objectives:
1. Working with service management
2. Implementing monitoring loops
3. Handling multiple services
4. Processing service metrics

Requirements:
1. Monitor multiple services per server
2. Check service status (running/stopped)
3. Track service uptime
4. Monitor resource usage per service
5. Generate service health reports

Hints:
1. Service Status Checking:
   - Windows: sc query servicename
   - Linux: systemctl status servicename
   - Handle both OS types

2. Resource Monitoring:
   - Track CPU usage per service
   - Monitor memory consumption
   - Check port availability
   - Track response times

3. Data Structure:
   {
       "server_name": {
           "service1": {
               "status": "running",
               "uptime": "5d 2h",
               "cpu_usage": "25%",
               "memory": "150MB"
           }
       }
   }

4. Implementation Tips:
   - Use subprocess for service checks
   - Implement timeout mechanisms
   - Add error handling for each check
   - Store historical data

5. Output Formatting:
   - Use tables for better readability
   - Color code status (green/yellow/red)
   - Include timestamp for each check

Bonus Challenges:
1. Add service dependency tracking
2. Implement service restart capability
3. Create service health trends
4. Add configuration file support

Tips:
- Use context managers for resources
- Implement proper error handling
- Add logging functionality
- Consider cross-platform compatibility
- Use async operations for better performance
"""

# Implement your solution here