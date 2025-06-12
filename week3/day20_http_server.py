"""
Day 20: HTTP Server - Log File Server

Objective:
Create a simple HTTP server that can serve log files and system information,
making it easy to view logs and metrics through a web browser.

Learning Objectives:
1. Using http.server module
2. Serving static files
3. Creating web endpoints
4. Handling requests

Detailed Instructions:
1. Server Setup (15 mins):
   - Import http.server
   - Create handler class
   - Set up server
   - Handle routing

2. File Serving (15 mins):
   - Serve log files
   - Add directories
   - Handle paths
   - Set content types

3. Request Handler (15 mins):
   - Process GET/POST
   - Parse parameters
   - Return responses
   - Handle errors

4. Security Features (15 mins):
   - Add authentication
   - Validate paths
   - Set permissions
   - Log access

Key Concepts:
1. HTTP Server:
   ```python
   from http.server import HTTPServer, SimpleHTTPRequestHandler
   
   class LogServer(SimpleHTTPRequestHandler):
       def do_GET(self):
           # Handle GET request
           self.send_response(200)
           self.end_headers()
   ```

2. File Handling:
   ```python
   def serve_file(self, path):
       with open(path, 'rb') as f:
           self.wfile.write(f.read())
   ```

Challenge Tasks:
1. Add authentication
2. Create API endpoints
3. Implement search
4. Add real-time logs

Tips for Success:
- Set proper headers
- Handle all methods
- Add error pages
- Log all access

Common Mistakes to Avoid:
- Security holes
- Missing headers
- No error handling
- Path traversal
"""

# Only necessary imports
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from typing import Dict, Optional

class LogServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle GET request
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")

def run(server_class=HTTPServer, handler_class=LogServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
