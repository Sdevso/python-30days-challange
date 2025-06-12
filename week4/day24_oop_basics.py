"""
Day 24: OOP Basics - Server Class Abstraction

Objective:
Create an object-oriented abstraction for server management, focusing on
encapsulation, inheritance, and polymorphism principles.

Learning Objectives:
1. Understanding OOP concepts
2. Creating class hierarchies
3. Implementing methods
4. Using inheritance

Detailed Instructions:
1. Class Basics (15 mins):
   - Create Server class
   - Add attributes
   - Define methods
   - Use constructor

2. Inheritance (15 mins):
   - Create base class
   - Implement child classes
   - Override methods
   - Use super()

3. Encapsulation (15 mins):
   - Private attributes
   - Property decorators
   - Protected methods
   - Data validation

4. Polymorphism (15 mins):
   - Abstract classes
   - Interface methods
   - Method overriding
   - Duck typing

Key Concepts:
1. Class Definition:
   ```python
   class Server:
       def __init__(self, name: str, ip: str):
           self.name = name
           self.ip = ip
           self._status = 'offline'
       
       @property
       def status(self) -> str:
           return self._status
   ```

2. Inheritance:
   ```python
   class WebServer(Server):
       def __init__(self, name: str, ip: str, port: int):
           super().__init__(name, ip)
           self.port = port
           
       def start(self):
           self._status = 'running'
   ```

Challenge Tasks:
1. Add server types
2. Implement monitoring
3. Create service class
4. Add state management

Tips for Success:
- Use proper encapsulation
- Plan class hierarchy
- Document methods
- Validate input data

Common Mistakes to Avoid:
- Deep inheritance
- Tight coupling
- Missing validation
- Poor encapsulation
"""

# Only necessary imports
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class Server(ABC):
    def __init__(self, name: str, ip: str):
        self.name = name
        self.ip = ip
        self._status = 'offline'
    
    @property
    def status(self) -> str:
        return self._status
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class WebServer(Server):
    def __init__(self, name: str, ip: str, port: int):
        super().__init__(name, ip)
        self.port = port
    
    def start(self):
        self._status = 'running'
    
    def stop(self):
        self._status = 'stopped'

class DBServer(Server):
    def __init__(self, name: str, ip: str, db_name: str):
        super().__init__(name, ip)
        self.db_name = db_name
    
    def start(self):
        self._status = 'running'
    
    def stop(self):
        self._status = 'stopped'

def monitor_servers(servers: List[Server]):
    for server in servers:
        print(f"Server {server.name} is {server.status}")

def main():
    web_server = WebServer("WebServer1", "192.168.1.1", 80)
    db_server = DBServer("DBServer1", "192.168.1.2", "MyDatabase")
    
    web_server.start()
    db_server.start()
    
    monitor_servers([web_server, db_server])

if __name__ == "__main__":
    main()
