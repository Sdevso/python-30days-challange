"""
Day 8: Error Handling in Server Operations

Challenge Description:
Create a robust error handling system for server operations that gracefully handles
various types of failures and provides meaningful error messages.

Learning Objectives:
1. Implement comprehensive error handling
2. Create custom exception classes
3. Use context managers
4. Develop error recovery strategies

Requirements:
1. Create custom exceptions for:
   - ServerConnectionError
   - ServiceStatusError
   - ConfigurationError
   - ResourceNotFoundError
   - PermissionError

2. Implement error handling for:
   - Network timeouts
   - Authentication failures
   - Resource constraints
   - Configuration issues
   - Permission problems

Hints:
1. Custom Exception Structure:
   class ServerError(Exception):
       def __init__(self, server, message):
           self.server = server
           self.message = message
           super().__init__(f"{server}: {message}")

2. Error Categories to Handle:
   - Network Errors:
     * Connection timeouts
     * DNS resolution failures
     * SSL certificate issues
   
   - Service Errors:
     * Service not running
     * Port not available
     * Resource exhaustion
   
   - Configuration Errors:
     * Missing config files
     * Invalid parameters
     * Version mismatches

3. Error Recovery Strategies:
   - Implement automatic retries
   - Use fallback options
   - Implement circuit breakers
   - Add timeout mechanisms

4. Logging and Reporting:
   - Log error details
   - Include stack traces
   - Add context information
   - Track error frequencies

Bonus Challenges:
1. Implement an error aggregation system
2. Create error severity levels
3. Add automated recovery actions
4. Implement error notifications

Tips:
- Use context managers for cleanup
- Implement proper error hierarchies
- Add detailed error messages
- Include system state in errors
- Consider using error codes
"""

class ServerNotFoundError(Exception):
    """Custom exception for when a server is not found in inventory"""
    pass

class ServiceNotRunningError(Exception):
    """Custom exception for when a required service is not running"""
    pass

def check_server_status(server_name):
    # TODO: Implement server status check with proper error handling
    pass

def main():
    try:
        # TODO: Implement main function with error handling
        pass
    except ServerNotFoundError as e:
        print(f"Error: {e}")
    except ServiceNotRunningError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
