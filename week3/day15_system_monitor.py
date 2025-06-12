"""
Day 15: System Monitor - Resource Tracker

Objective:
Build a system resource monitor that can track CPU, memory, and disk usage,
with alerts when thresholds are exceeded.

Learning Objectives:
1. Using psutil library
2. Monitoring system resources
3. Setting up alerts
4. Tracking performance

Detailed Instructions:
1. System Metrics (15 mins):
   - Install psutil
   - Get CPU usage
   - Monitor memory
   - Check disk space

2. Resource Tracking (15 mins):
   - Set up monitoring loop
   - Record metrics
   - Calculate averages
   - Track trends

3. Alert System (15 mins):
   - Define thresholds
   - Create alert logic
   - Send notifications
   - Log alerts

4. Performance Data (15 mins):
   - Store metrics
   - Create reports
   - Visualize data
   - Track history

Key Concepts:
1. Resource Monitoring:
   ```python
   import psutil
   
   # CPU usage
   cpu_percent = psutil.cpu_percent(interval=1)
   
   # Memory usage
   memory = psutil.virtual_memory()
   memory_percent = memory.percent
   ```

2. Alert Logic:
   ```python
   def check_threshold(value, threshold):
       return value > threshold
   
   # Example usage
   CPU_THRESHOLD = 80
   if check_threshold(cpu_percent, CPU_THRESHOLD):
       send_alert("CPU Usage High")
   ```

Challenge Tasks:
1. Monitor multiple metrics
2. Create alert levels
3. Generate reports
4. Implement logging

Tips for Success:
- Set proper intervals
- Use appropriate thresholds
- Handle errors gracefully
- Store historical data

Common Mistakes to Avoid:
- Too frequent checks
- Missing error handling
- No data persistence
- Hard-coded values
"""

# Only necessary imports
import psutil
import time
from typing import Dict, List, Optional

# CPU monitoring class
class CPUMonitor:
    def __init__(self, warning_threshold: float = 80.0, critical_threshold: float = 90.0):
        """Initialize CPU monitor with thresholds.
        
        Args:
            warning_threshold: CPU usage % for warning (default: 80%)
            critical_threshold: CPU usage % for critical alert (default: 90%)
        """
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.alert_history: List[Dict] = []

    def check_cpu_usage(self) -> Dict:
        """Check current CPU usage and return status."""
        cpu_percent = psutil.cpu_percent(interval=1)
        status = self._determine_status(cpu_percent)
        
        return {
            "timestamp": time.time(),
            "cpu_percent": cpu_percent,
            "status": status,
            "per_cpu": psutil.cpu_percent(interval=1, percpu=True)
        }

    def _determine_status(self, cpu_percent: float) -> str:
        """Determine alert status based on CPU usage."""
        if cpu_percent >= self.critical_threshold:
            return "CRITICAL"
        elif cpu_percent >= self.warning_threshold:
            return "WARNING"
        return "OK"

# Usage example
monitor = CPUMonitor(warning_threshold=75, critical_threshold=85)
result = monitor.check_cpu_usage()
print(f"CPU Usage: {result['cpu_percent']}% - Status: {result['status']}")
