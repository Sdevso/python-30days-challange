"""
Day 26: SDKs & Cloud - Cloud Resource Manager

Objective:
Build a cloud resource management system using AWS/Azure SDKs to list, monitor,
and manage cloud resources effectively.

Learning Objectives:
1. Using cloud SDKs
2. Managing resources
3. Handling credentials
4. Monitoring usage

Detailed Instructions:
1. SDK Setup (15 mins):
   - Install SDK
   - Configure auth
   - Test connection
   - Handle errors

2. Resource Management (15 mins):
   - List resources
   - Get details
   - Monitor status
   - Track usage

3. Operations (15 mins):
   - Start/stop
   - Create/delete
   - Update config
   - Tag resources

4. Monitoring (15 mins):
   - Check metrics
   - Set alerts
   - Track costs
   - Generate reports

Key Concepts:
1. AWS SDK:
   ```python
   import boto3
   
   # Initialize client
   ec2 = boto3.client('ec2')
   
   # List instances
   response = ec2.describe_instances()
   ```

2. Azure SDK:
   ```python
   from azure.mgmt.compute import ComputeManagementClient
   
   # Initialize client
   compute_client = ComputeManagementClient(
       credential,
       subscription_id
   )
   ```

Challenge Tasks:
1. Multi-cloud support
2. Cost optimization
3. Auto-scaling
4. Resource tracking

Tips for Success:
- Secure credentials
- Handle rate limits
- Add error handling
- Monitor costs

Common Mistakes to Avoid:
- Exposed secrets
- Missing cleanup
- Poor error handling
- Resource leaks
"""

# Only necessary imports
import boto3
from azure.mgmt.compute import ComputeManagementClient
from typing import Dict, List, Any, Optional

class CloudResourceManager:
    def __init__(self, cloud_provider: str, credentials: Dict[str, str]):
        self.cloud_provider = cloud_provider
        self.credentials = credentials
        self.resource_clients = {}
        self.initialize_sdk()
    
    def initialize_sdk(self):
        if self.cloud_provider == "aws":
            # Initialize AWS SDK
            self.resource_clients['ec2'] = boto3.client('ec2', **self.credentials)
        elif self.cloud_provider == "azure":
            # Initialize Azure SDK
            self.resource_clients['compute'] = ComputeManagementClient(
                credential=self.credentials['credential'],
                subscription_id=self.credentials['subscription_id']
            )
        else:
            raise ValueError("Unsupported cloud provider")
    
    def list_resources(self):
        if self.cloud_provider == "aws":
            # List EC2 instances in AWS
            return self.resource_clients['ec2'].describe_instances()
        elif self.cloud_provider == "azure":
            # List virtual machines in Azure
            return self.resource_clients['compute'].list()
        else:
            raise ValueError("Unsupported cloud provider")
    
    def start_resource(self, resource_id: str):
        if self.cloud_provider == "aws":
            # Start an EC2 instance in AWS
            self.resource_clients['ec2'].start_instances(InstanceIds=[resource_id])
        elif self.cloud_provider == "azure":
            # Start a virtual machine in Azure
            self.resource_clients['compute'].start(resource_id)
        else:
            raise ValueError("Unsupported cloud provider")
    
    def stop_resource(self, resource_id: str):
        if self.cloud_provider == "aws":
            # Stop an EC2 instance in AWS
            self.resource_clients['ec2'].stop_instances(InstanceIds=[resource_id])
        elif self.cloud_provider == "azure":
            # Stop a virtual machine in Azure
            self.resource_clients['compute'].stop(resource_id)
        else:
            raise ValueError("Unsupported cloud provider")

def main():
    # Example usage
    aws_credentials = {
        'aws_access_key_id': 'YOUR_AWS_ACCESS_KEY',
        'aws_secret_access_key': 'YOUR_AWS_SECRET_KEY',
        'region_name': 'YOUR_AWS_REGION'
    }
    
    azure_credentials = {
        'credential': 'YOUR_AZURE_CREDENTIAL',
        'subscription_id': 'YOUR_AZURE_SUBSCRIPTION_ID'
    }
    
    # AWS Resource Manager
    aws_manager = CloudResourceManager("aws", aws_credentials)
    print(aws_manager.list_resources())
    
    # Azure Resource Manager
    azure_manager = CloudResourceManager("azure", azure_credentials)
    print(azure_manager.list_resources())

if __name__ == "__main__":
    main()

"""
Hints:
1. SDK Setup:
   - Install AWS SDK: `pip install boto3`
   - Install Azure SDK: `pip install azure-mgmt-compute`

2. Resource Management:
   - Use `describe_instances()` for AWS to list instances
   - Use `list()` for Azure to list virtual machines

3. Operations:
   - Use `start_instances()` and `stop_instances()` for AWS to manage instances
   - Use `start()` and `stop()` for Azure to manage virtual machines

4. Monitoring:
   - Use AWS CloudWatch and Azure Monitor for tracking metrics and setting alerts

Bonus Challenges:
1. Multi-cloud deployment scripts
2. Cost optimization recommendations
3. Auto-scaling based on metrics
4. Resource usage reporting

Tips:
- Securely manage credentials using environment variables or secret management tools
- Handle API rate limits and errors gracefully
- Monitor and optimize resource usage to manage costs
"""
