"""
Day 16: File Backup - Config Backup System

Objective:
Create an automated file backup system that can copy important configuration
files and add timestamps to backup versions.

Learning Objectives:
1. Using shutil operations
2. Working with timestamps
3. Managing file paths
4. Organizing backups

Detailed Instructions:
1. File Operations (15 mins):
   - Import shutil
   - Copy files
   - Create directories
   - Handle paths

2. Backup Strategy (15 mins):
   - Add timestamps
   - Organize backups
   - Manage versions
   - Handle duplicates

3. Error Handling (15 mins):
   - Check file existence
   - Handle permissions
   - Manage space
   - Log operations

4. Backup Management (15 mins):
   - Clean old backups
   - Verify copies
   - Restore files
   - Track changes

Key Concepts:
1. File Operations:
   ```python
   import shutil
   from datetime import datetime
   
   # Create timestamped backup
   timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
   backup_name = f'config_{timestamp}.bak'
   
   # Copy file
   shutil.copy2('config.ini', backup_name)
   ```

2. Directory Management:
   ```python
   import os
   
   # Create backup directory
   backup_dir = 'backups'
   os.makedirs(backup_dir, exist_ok=True)
   
   # Clean old backups
   for file in os.listdir(backup_dir):
       if file.endswith('.bak'):
           file_path = os.path.join(backup_dir, file)
           # Add cleanup logic
   ```

Challenge Tasks:
1. Add compression
2. Implement rotation
3. Create restore function
4. Add change detection

Tips for Success:
- Use absolute paths
- Add error handling
- Verify backups
- Clean old files

Common Mistakes to Avoid:
- Hardcoded paths
- No error checks
- Missing permissions
- Space issues
"""

# Only necessary imports
import os
import shutil
from datetime import datetime
from typing import List, Optional

class ConfigBackup:
    def __init__(self, backup_dir: str):
        """Initialize backup system.
        
        Args:
            backup_dir: Directory to store backups
        """
        self.backup_dir = backup_dir
        self._ensure_backup_dir()

    def _ensure_backup_dir(self):
        """Create backup directory if it doesn't exist."""
        os.makedirs(self.backup_dir, exist_ok=True)

    def create_backup(self, source_path: str) -> Optional[str]:
        """Create a timestamped backup of a file.
        
        Args:
            source_path: Path to file to backup
            
        Returns:
            Path to backup file or None if failed
        """
        try:
            # Create timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Get file name and new backup name
            file_name = os.path.basename(source_path)
            backup_name = f"{file_name}_{timestamp}.bak"
            backup_path = os.path.join(self.backup_dir, backup_name)
            
            # Copy file
            shutil.copy2(source_path, backup_path)
            return backup_path
        except Exception as e:
            print(f"Backup failed: {str(e)}")
            return None

    def list_backups(self, file_name: str) -> List[str]:
        """List all backups for a specific file."""
        backups = []
        for f in os.listdir(self.backup_dir):
            if f.startswith(file_name):
                backups.append(f)
        return sorted(backups)

    def backup_file(self, src: str) -> str:
        """Backup a single file with timestamp.
        
        Args:
            src: Source file path
            
        Returns:
            Backup file path
        """
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        file_name = os.path.basename(src)
        backup_name = f"{file_name}_{timestamp}"
        backup_path = os.path.join(self.backup_dir, backup_name)
        shutil.copy2(src, backup_path)
        return backup_path

    def backup_directory(self, src_dir: str):
        """Backup an entire directory with timestamp.
        
        Args:
            src_dir: Source directory path
        """
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        dir_name = os.path.basename(src_dir)
        backup_name = f"{dir_name}_{timestamp}"
        backup_path = os.path.join(self.backup_dir, backup_name)
        shutil.copytree(src_dir, backup_path)

    def verify_backup(self, src: str, backup: str) -> bool:
        """Verify if the backup is identical to the source.
        
        Args:
            src: Source file/directory path
            backup: Backup file/directory path
            
        Returns:
            True if backup is valid, False otherwise
        """
        if not os.path.exists(backup):
            return False
        if os.path.isfile(src):
            return filecmp.cmp(src, backup, shallow=False)
        return all(
            filecmp.cmp(
                os.path.join(src, f),
                os.path.join(backup, f),
                shallow=False
            )
            for f in os.listdir(src)
        )

def main():
    # Example configuration
    backup_config = {
        'source_path': '/etc/nginx',
        'backup_dir': '/var/backups/nginx',
        'max_backups': 5,
        'compression': True
    }

if __name__ == "__main__":
    main()
