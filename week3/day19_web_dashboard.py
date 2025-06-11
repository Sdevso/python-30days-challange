"""
Day 19: Real-time Monitoring Dashboard

Challenge Description:
Build a modern, responsive web dashboard that provides real-time insights into
your server infrastructure. Create an intuitive interface that helps operators
quickly identify and respond to issues.

Learning Objectives:
1. Create web applications with Flask
2. Implement real-time updates
3. Design responsive interfaces
4. Handle user authentication

Requirements:
1. Core Dashboard Features:
   - Server status overview
   - Real-time metrics graphs
   - Alert notifications
   - Service status panels

2. Technical Implementation:
   - RESTful API backend
   - WebSocket updates
   - Responsive design
   - Secure authentication

Skills:
- Flask framework
- HTML/CSS
- Basic authentication
- Server-side rendering

Instructions:
1. Create Flask application structure
2. Implement dashboard routes
3. Create HTML templates
4. Add basic authentication
"""

from flask import Flask, render_template, jsonify, request, session
from functools import wraps
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change in production

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def dashboard():
    # TODO: Implement dashboard view
    pass

@app.route('/api/servers')
@login_required
def get_servers():
    # TODO: Implement server status API
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Implement login functionality
    pass

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

"""
Hints:
1. Flask Route Structure:
   @app.route('/api/servers')
   @login_required
   def get_servers():
       servers = fetch_server_status()
       return jsonify(servers)

2. WebSocket Updates:
   @socketio.on('connect')
   def handle_connect():
       if 'user_id' not in session:
           return False
       join_room('monitoring')
       emit('status', get_current_status())

3. Dashboard Layout:
   ```html
   <div class="dashboard-grid">
     <div class="server-overview">
       <h2>Server Status</h2>
       <div class="status-cards">
         <!-- Dynamic server cards -->
       </div>
     </div>
     <div class="metrics-panel">
       <canvas id="metricsChart"></canvas>
     </div>
   </div>
   ```

4. Authentication System:
   def authenticate():
       token = request.headers.get('Authorization')
       if not token:
           abort(401)
       return validate_token(token)

Bonus Challenges:
1. Add custom dashboards
2. Implement dark mode
3. Create mobile app view
4. Add export capabilities
5. Implement user roles

Tips:
- Use CSS Grid/Flexbox
- Add loading states
- Implement error handling
- Cache API responses
- Add search/filter
- Use async data loading
"""
