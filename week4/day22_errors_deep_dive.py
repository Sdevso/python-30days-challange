"""
Day 22: Errors Deep Dive - Advanced Error Handling

Objective:
Master advanced error handling techniques by creating custom exceptions,
implementing retry mechanisms, and building robust error recovery systems.

Learning Objectives:
1. Creating custom exceptions
2. Implementing retry logic
3. Building error recovery
4. Managing error hierarchies

Detailed Instructions:
1. Custom Exceptions (15 mins):
   - Create base exceptions
   - Add custom attributes
   - Implement error messages
   - Build hierarchy

2. Retry Mechanism (15 mins):
   - Implement backoff
   - Add max retries
   - Handle timeouts
   - Log attempts

3. Error Recovery (15 mins):
   - Create recovery plans
   - Handle state
   - Clean up resources
   - Restore operations

4. Advanced Features (15 mins):
   - Chain exceptions
   - Add context
   - Create error reports
   - Track frequency

Key Concepts:
1. Custom Exceptions:
   ```python
   class ServiceError(Exception):
       def __init__(self, service: str, message: str):
           self.service = service
           self.message = message
           super().__init__(f"{service}: {message}")
   
   class RetryableError(ServiceError):
       def __init__(self, service: str, attempts: int):
           super().__init__(service, f"Failed after {attempts} attempts")
   ```

2. Retry Logic:
   ```python
   def retry_operation(func, max_attempts: int = 3):
       attempt = 0
       while attempt < max_attempts:
           try:
               return func()
           except RetryableError:
               attempt += 1
               if attempt == max_attempts:
                   raise
   ```

Challenge Tasks:
1. Add circuit breaker
2. Implement fallbacks
3. Create error tracking
4. Build recovery system

Tips for Success:
- Define clear hierarchies
- Add proper context
- Log all attempts
- Plan recovery steps

Common Mistakes to Avoid:
- Catching too broadly
- Missing cleanup
- Hiding root cause
- No retry limits
"""

# Only necessary imports
from typing import Any, Callable, Dict, Optional
import time
import logging

# Custom exception classes
class ServiceError(Exception):
    """Base class for service-related errors."""
    def __init__(self, service: str, message: str):
        self.service = service
        self.message = message
        super().__init__(f"{service}: {message}")

class RetryableError(ServiceError):
    """Exception indicating a retryable error."""
    def __init__(self, service: str, attempts: int):
        super().__init__(service, f"Failed after {attempts} attempts")

# Retry mechanism with exponential backoff
def retry_operation(func: Callable[[], Any], max_attempts: int = 3, base_delay: int = 1, max_delay: int = 16) -> Any:
    """Retry a function call with exponential backoff."""
    attempt = 0
    while attempt < max_attempts:
        try:
            return func()
        except RetryableError:
            attempt += 1
            delay = min(base_delay * 2 ** attempt, max_delay)
            logging.warning(f"Attempt {attempt} failed, retrying in {delay} seconds...")
            time.sleep(delay)
            if attempt == max_attempts:
                raise

# Example recovery function
def recoverable_operation():
    """An example operation that may fail and requires recovery."""
    # TODO: Implement the operation logic
    pass

# Recovery plan
def recovery_plan():
    """Execute the recovery plan."""
    try:
        recoverable_operation()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        # TODO: Implement recovery steps
        pass

def main():
    # TODO: Implement main function to demonstrate error handling
    pass

if __name__ == "__main__":
    main()
