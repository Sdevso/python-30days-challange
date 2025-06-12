"""
Day 17: Email Alert - Disk Space Monitor

Objective:
Create an email alert system that monitors disk space and sends notifications
when storage usage exceeds defined thresholds.

Learning Objectives:
1. Working with SMTP
2. Sending email alerts
3. Monitoring disk space
4. Creating HTML emails

Detailed Instructions:
1. Email Setup (15 mins):
   - Configure SMTP
   - Set up credentials
   - Test connection
   - Handle security

2. Alert Content (15 mins):
   - Create templates
   - Format messages
   - Add HTML content
   - Include data

3. Disk Monitoring (15 mins):
   - Check usage
   - Set thresholds
   - Track changes
   - Format data

4. Alert Logic (15 mins):
   - Define rules
   - Set frequencies
   - Handle repeats
   - Log alerts

Key Concepts:
1. Email Configuration:
   ```python
   import smtplib
   from email.mime.text import MIMEText
   
   # Setup SMTP
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   
   # Login
   server.login('user@example.com', 'password')
   ```

2. Alert Message:
   ```python
   def create_alert(usage: float) -> str:
       return f'''
       <h2>Disk Space Alert</h2>
       <p>Usage: {usage}%</p>
       '''
   ```

Challenge Tasks:
1. Add multiple alerts
2. Create HTML templates
3. Implement rate limiting
4. Add attachments

Tips for Success:
- Use app passwords
- Test email delivery
- Format HTML properly
- Handle bounces

Common Mistakes to Avoid:
- Hard-coded credentials
- No error handling
- Plain text only
- Missing rate limits
"""

# Only necessary imports
import smtplib
import psutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, Optional

def setup_smtp(host: str, port: int, username: str, password: str):
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(username, password)
    return server

def check_disk_usage(path: str = '/') -> float:
    disk = psutil.disk_usage(path)
    return disk.percent

def create_email_body(disk_data: dict) -> str:
    return f'''
        <html>
        <body>
        <h2>Disk Usage Alert</h2>
        <p>The following disks are running low on space:</p>
        <ul>
        {disk_data_to_html(disk_data)}
        </ul>
        </body>
        </html>
        '''

def send_alert(smtp_server, from_addr: str, to_addr: str, subject: str, body: str):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    smtp_server.send_message(msg)

def disk_data_to_html(disk_data: dict) -> str:
    html = ""
    for path, usage in disk_data.items():
        html += f"<li>{path}: {usage}% used</li>"
    return html

def main():
    # Example configuration
    smtp_config = {
        'host': 'smtp.gmail.com',
        'port': 587,
        'username': 'your-email@gmail.com',
        'password': 'your-app-password'
    }
    
    alert_config = {
        'warning_threshold': 80.0,
        'critical_threshold': 90.0,
        'check_paths': ['/', '/home'],
        'to_email': 'admin@example.com'
    }
    
    try:
        # Set up SMTP server
        smtp_server = setup_smtp(
            smtp_config['host'],
            smtp_config['port'],
            smtp_config['username'],
            smtp_config['password']
        )
        
        # Check disk usage
        disk_usage_data = {path: check_disk_usage(path) for path in alert_config['check_paths']}
        
        # Determine if alert is needed
        for path, usage in disk_usage_data.items():
            if usage >= alert_config['critical_threshold']:
                send_alert(
                    smtp_server,
                    smtp_config['username'],
                    alert_config['to_email'],
                    "Critical Disk Usage Alert",
                    create_email_body(disk_usage_data)
                )
            elif usage >= alert_config['warning_threshold']:
                send_alert(
                    smtp_server,
                    smtp_config['username'],
                    alert_config['to_email'],
                    "Warning Disk Usage Alert",
                    create_email_body(disk_usage_data)
                )
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        smtp_server.quit()

if __name__ == "__main__":
    main()
