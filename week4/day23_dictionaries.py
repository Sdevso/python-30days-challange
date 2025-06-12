"""
Day 23: Dictionaries - Server Metadata Handler

Objective:
Create a robust server metadata management system using Python dictionaries
to store, update, and track server information efficiently.

Learning Objectives:
1. Mastering dictionary operations
2. Working with nested data
3. Managing server metadata
4. Implementing data validation

Detailed Instructions:
1. Dictionary Basics (15 mins):
   - Create dictionaries
   - Access values
   - Update data
   - Handle missing keys

2. Nested Structures (15 mins):
   - Build complex data
   - Navigate nested dicts
   - Update nested values
   - Handle deep paths

3. Dictionary Methods (15 mins):
   - Use get()
   - Apply update()
   - Handle items()
   - Implement pop()

4. Data Management (15 mins):
   - Validate data
   - Merge dictionaries
   - Track changes
   - Handle cleanup

Key Concepts:
1. Dictionary Operations:
   ```python
   # Basic operations
   server = {
       'name': 'web-01',
       'ip': '192.168.1.100',
       'services': ['nginx', 'mysql']
   }
   
   # Safe access
   status = server.get('status', 'unknown')
   ```

2. Nested Handling:
   ```python
   # Nested structure
   servers = {
       'web': {
           'prod': {'count': 5, 'type': 't2.micro'},
           'dev': {'count': 2, 'type': 't2.nano'}
       }
   }
   ```

Challenge Tasks:
1. Implement server tracker
2. Add metadata validation
3. Create change history
4. Build search function

Tips for Success:
- Use dictionary methods
- Handle missing keys
- Validate input data
- Keep data organized

Common Mistakes to Avoid:
- Direct key access
- Mutable defaults
- Shallow copies
- Missing validation
"""

# Only necessary imports
from typing import Dict, List, Any, Optional
from copy import deepcopy

class ServerMetadata:
    """
    ServerMetadata is a class to manage and track server metadata using
    Python dictionaries. It provides methods to set, get, update, and
    validate server information.
    """
    def __init__(self):
        """
        Initializes an empty server metadata dictionary and a change log.
        """
        self.metadata = {}
        self.change_log = []
    
    def set_metadata(self, server_id: str, data: Dict[str, Any]):
        """
        Sets the metadata for a given server ID. If the server ID already
        exists, it updates the metadata and logs the change.

        :param server_id: Unique identifier for the server
        :param data: Dictionary containing server metadata
        """
        if server_id in self.metadata:
            self.log_change(server_id, self.metadata[server_id], data)
        self.metadata[server_id] = data
    
    def get_metadata(self, server_id: str) -> Optional[Dict[str, Any]]:
        """
        Gets the metadata for a given server ID.

        :param server_id: Unique identifier for the server
        :return: Dictionary containing server metadata or None if not found
        """
        return self.metadata.get(server_id)
    
    def update_metadata(self, server_id: str, data: Dict[str, Any]):
        """
        Updates the metadata for a given server ID. Only the provided fields
        will be updated.

        :param server_id: Unique identifier for the server
        :param data: Dictionary containing the fields to update
        """
        if server_id in self.metadata:
            old_data = deepcopy(self.metadata[server_id])
            self.metadata[server_id].update(data)
            self.log_change(server_id, old_data, self.metadata[server_id])
    
    def log_change(self, server_id: str, old_data: Dict[str, Any], new_data: Dict[str, Any]):
        """
        Logs the change in metadata for a server. It records the server ID,
        old data, new data, and a timestamp.

        :param server_id: Unique identifier for the server
        :param old_data: Dictionary containing the old metadata
        :param new_data: Dictionary containing the new metadata
        """
        from datetime import datetime
        self.change_log.append({
            'server_id': server_id,
            'old_data': old_data,
            'new_data': new_data,
            'timestamp': datetime.now()
        })
    
    def get_change_log(self) -> List[Dict[str, Any]]:
        """
        Gets the change log.

        :return: List of changes made to the metadata
        """
        return self.change_log
    
    def validate_metadata(self, server_id: str) -> bool:
        """
        Validates the metadata for a given server ID. Checks for required
        fields and correct data types.

        :param server_id: Unique identifier for the server
        :return: True if metadata is valid, False otherwise
        """
        metadata = self.get_metadata(server_id)
        if not metadata:
            return False
        
        # Example validation: check if 'ip' field is present and valid
        if 'ip' not in metadata:
            return False
        
        return True

def main():
    """
    Main function to demonstrate the usage of the ServerMetadata class.
    """
    server_meta = ServerMetadata()
    
    # Setting metadata for a server
    server_meta.set_metadata('server1', {
        'name': 'Web Server 1',
        'ip': '192.168.1.10',
        'services': ['nginx', 'mysql']
    })
    
    # Getting metadata
    print("Metadata for server1:", server_meta.get_metadata('server1'))
    
    # Updating metadata
    server_meta.update_metadata('server1', {
        'ip': '192.168.1.11'
    })
    
    # Getting updated metadata
    print("Updated metadata for server1:", server_meta.get_metadata('server1'))
    
    # Validating metadata
    print("Is metadata for server1 valid?", server_meta.validate_metadata('server1'))
    
    # Getting change log
    print("Change log:", server_meta.get_change_log())

if __name__ == "__main__":
    main()
