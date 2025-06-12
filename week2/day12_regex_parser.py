"""
Day 12: Shell Commands - System Command Handler

Objective:
Create a robust system command handler that can execute various shell commands,
process their output, and handle different platforms safely.

Learning Objectives:
1. Using subprocess.run()
2. Managing command execution
3. Handling command output
4. Cross-platform commands

Detailed Instructions:
1. Basic Command Execution (15 mins):
   - Use subprocess.run()
   - Capture command output
   - Check return codes
   - Handle errors

2. Platform Handling (15 mins):
   - Detect operating system
   - Adjust commands
   - Handle differences
   - Test compatibility

3. Output Processing (15 mins):
   - Parse command output
   - Extract information
   - Format results
   - Handle encoding

4. Advanced Features (15 mins):
   - Set timeouts
   - Handle signals
   - Chain commands
   - Stream output

Key Concepts:
1. Command Execution:
   ```python
   # Basic command running
   import subprocess
   
   result = subprocess.run(
       ['ping', '-n', '1', 'localhost'],
       capture_output=True,
       text=True
   )
   ```

2. Platform Handling:
   ```python
   # Cross-platform command
   import sys
   
   ping_cmd = ['ping', '-n' if sys.platform == 'win32' else '-c', '1']
   ```

Challenge Tasks:
1. Create command chains
2. Add progress tracking
3. Implement timeouts
4. Handle long output

Tips for Success:
- Always handle errors
- Check return codes
- Set timeouts
- Use proper encoding

Common Mistakes to Avoid:
- Shell injection risks
- Missing error checks
- Platform assumptions
- Resource leaks
"""

# Only necessary imports
import subprocess
import sys
from typing import Dict, List, Optional

class CommandResult:
    """Class to represent the result of a command execution."""
    def __init__(self, stdout: str, stderr: str, returncode: int):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode

    def __repr__(self):
        return f"<CommandResult returncode={self.returncode}>"

def run_command(command: List[str], timeout: Optional[int] = 30) -> CommandResult:
    """Run a system command and return the result."""
    try:
        # Run command and capture output
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return CommandResult(result.stdout, result.stderr, result.returncode)
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds")
        return CommandResult("", "Command timed out", -1)
    except Exception as e:
        print(f"Error running command: {str(e)}")
        return CommandResult("", str(e), -1)

def ping(hostname: str) -> CommandResult:
    """Ping a hostname and return the result."""
    command = ["ping", "-n" if sys.platform == "win32" else "-c", "1", hostname]
    return run_command(command)

def check_service(service_name: str) -> CommandResult:
    """Check the status of a service and return the result."""
    command = ["sc", "query", service_name] if sys.platform == "win32" else ["systemctl", "status", service_name]
    return run_command(command)

def main():
    """Main function to demonstrate command handling."""
    # Example: Ping localhost
    result = ping("localhost")
    print(f"Ping result: {result}")

    # Example: Check service status
    service_name = "wuauserv"  # Windows Update Service
    result = check_service(service_name)
    print(f"Service status: {result}")

if __name__ == "__main__":
    main()
