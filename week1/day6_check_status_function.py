"""
Day 6: Status Check Functions

Challenge Description:
Create a library of reusable functions for checking various aspects of server status.
Focus on creating modular, well-documented, and reusable code that can be imported
into other scripts.

Learning Objectives:
1. Function design and modularity
2. Creating reusable code
3. Writing function documentation
4. Implementing return types
5. Error handling in functions

Requirements:
1. Create functions for:
   - Server connectivity check
   - Service status verification
   - Resource utilization check
   - Log file analysis
   - Alert generation

2. Each function should:
   - Have clear documentation
   - Include type hints
   - Handle errors gracefully
   - Return well-structured data

Hints:
1. Function Structure:
   def check_server_status(
       hostname: str,
       port: int = 22,
       timeout: float = 5.0
   ) -> Dict[str, Any]:
       '''
       Check server connectivity and basic health.
       
       Args:
           hostname: Server hostname or IP
           port: Port to check
           timeout: Connection timeout
           
       Returns:
           Dictionary with status information
       '''

2. Error Handling:
   - Use try/except blocks
   - Create custom exceptions
   - Return error status in results
   - Log errors appropriately

3. Return Data Structure:
   {
       'status': 'up'/'down',
       'response_time': 0.023,
       'last_check': '2025-06-10 10:00:00',
       'error': None or 'error message'
   }

4. Documentation:
   - Use docstrings for all functions
   - Include usage examples
   - Document exceptions
   - Add type hints

Bonus Challenges:
1. Add async versions of functions
2. Create function decorators for:
   - Retry logic
   - Caching
   - Logging
3. Add parameter validation
4. Create test functions

Tips:
- Keep functions focused and single-purpose
- Use descriptive function and parameter names
- Add timeout to all network operations
- Include status codes in returns
- Consider making a class for related functions
"""

# Implement your solution here