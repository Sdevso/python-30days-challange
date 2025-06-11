"""
Day 18: Alert Notification System

Challenge Description:
Build a comprehensive notification system that can alert system administrators
about server issues through multiple channels including email, SMS, and chat
platforms. Focus on reliable delivery and proper formatting.

Learning Objectives:
1. Design notification systems
2. Implement multiple channels
3. Handle message formatting
4. Ensure delivery reliability

Requirements:
1. Support Multiple Channels:
   - Email notifications
   - SMS alerts (via API)
   - Slack/Teams integration
   - Webhook support

2. Message Formatting:
   - Plain text
   - HTML formatting
   - Rich templates
   - Dynamic content

Hints:
1. Email Configuration:
   email_config = {
       'smtp_server': 'smtp.gmail.com',
       'smtp_port': 587,
       'username': 'alerts@company.com',
       'password': 'secure_password',
       'use_tls': True
   }

2. HTML Template Example:
   template = '''
   <html>
     <body>
       <h2>Server Alert</h2>
       <p>Status: {status}</p>
       <p>Server: {server}</p>
       <p>Time: {timestamp}</p>
       <p>Details: {details}</p>
     </body>
   </html>
   '''

3. Channel Integration:
   class NotificationChannel:
       def send_alert(self, message, level, recipients):
           raise NotImplementedError
   
   class EmailChannel(NotificationChannel):
       def send_alert(self, message, level, recipients):
           # Implement email sending
           pass

4. Message Priority:
   PRIORITY_LEVELS = {
       'critical': {'retry': 3, 'channels': ['email', 'sms', 'slack']},
       'warning': {'retry': 2, 'channels': ['email', 'slack']},
       'info': {'retry': 1, 'channels': ['email']}
   }

Bonus Challenges:
1. Add delivery confirmation
2. Implement message queuing
3. Create notification groups
4. Add message scheduling

Tips:
- Use async sending
- Implement retries
- Handle attachments
- Add rate limiting
- Log all notifications
- Email formatting
- HTML templates
- SMTP configuration

Instructions:
1. Create email notification system
2. Implement HTML email templates
3. Add support for attachments
4. Configure SMTP settings
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import List, Dict
import os

class EmailNotifier:
    def __init__(self, smtp_config: Dict[str, str]):
        self.smtp_config = smtp_config
        self.template_dir = "templates"
    
    def load_template(self, template_name: str) -> str:
        # TODO: Implement template loading
        pass
    
    def format_alert(self, alert_data: Dict[str, str]) -> str:
        # TODO: Implement alert formatting
        pass
    
    def send_alert(self, recipients: List[str], subject: str, body: str, attachments: List[str] = None):
        # TODO: Implement email sending
        pass

def main():
    # TODO: Implement main function to demonstrate email notifications
    pass

if __name__ == "__main__":
    main()
