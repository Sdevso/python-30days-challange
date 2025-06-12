"""
Day 19: Git Operations - Repository Manager

Objective:
Create an automated Git operations manager that can handle pulls, check logs,
and monitor repository status using Python's subprocess module.

Learning Objectives:
1. Running Git commands
2. Checking repo status
3. Managing branches
4. Monitoring changes

Detailed Instructions:
1. Git Commands (15 mins):
   - Run basic commands
   - Check status
   - Handle output
   - Process errors

2. Repository Ops (15 mins):
   - Pull updates
   - Check branches
   - Monitor logs
   - Track changes

3. Error Handling (15 mins):
   - Handle conflicts
   - Check permissions
   - Manage remotes
   - Log issues

4. Change Monitor (15 mins):
   - Track commits
   - Watch branches
   - Check stashes
   - Monitor tags

Key Concepts:
1. Git Operations:
   ```python
   import subprocess
   
   def run_git(command: List[str]) -> str:
       result = subprocess.run(
           ['git'] + command,
           capture_output=True,
           text=True
       )
       return result.stdout
   ```

2. Status Checking:
   ```python
   # Check repo status
   status = run_git(['status', '--porcelain'])
   if status:
       print("Changes detected")
   ```

Challenge Tasks:
1. Add auto-pull
2. Monitor branches
3. Track commit logs
4. Handle merges

Tips for Success:
- Check git installed
- Handle permissions
- Log all operations
- Verify commands

Common Mistakes to Avoid:
- No error handling
- Missing checks
- Unsafe operations
- Lost changes
"""

# Only necessary imports
import subprocess
import os
from typing import List, Optional

def run_git(command: List[str]) -> str:
    """Run a git command and return the output."""
    result = subprocess.run(
        ['git'] + command,
        capture_output=True,
        text=True
    )
    return result.stdout

def check_status() -> None:
    """Check the status of the git repository."""
    status = run_git(['status', '--porcelain'])
    if status:
        print("Changes detected")
    else:
        print("No changes")
