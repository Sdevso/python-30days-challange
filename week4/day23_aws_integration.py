"""
Day 23: Cloud Infrastructure Automation

Challenge Description:
Create a comprehensive cloud automation system using AWS services. Build
tools to manage infrastructure, monitor resources, and automate routine
operations in a cloud environment.

Learning Objectives:
1. Master AWS SDK (boto3)
2. Manage cloud resources
3. Monitor cloud metrics
4. Implement automation

Requirements:
1. Resource Management:
   - EC2 instances
   - S3 storage
   - Security groups
   - Load balancers

2. Monitoring & Metrics:
   - Resource usage
   - Cost tracking
   - Performance metrics
   - Alert thresholds

Skills:
- boto3
- AWS SDK
- Cloud resource management
- AWS service integration

Instructions:
1. Implement AWS client wrapper
2. Add EC2 management functions
3. Implement S3 operations
4. Add CloudWatch monitoring

Hints:
1. EC2 Management:
   def launch_instance(
       image_id: str,
       instance_type: str,
       key_name: str,
       security_groups: List[str]
   ) -> Dict[str, Any]:
       return ec2.run_instances(
           ImageId=image_id,
           InstanceType=instance_type,
           KeyName=key_name,
           SecurityGroups=security_groups,
           MinCount=1,
           MaxCount=1
       )

2. S3 Operations:
   def manage_bucket(
       bucket_name: str,
       action: str,
       file_path: str = None
   ):
       if action == 'create':
           s3.create_bucket(Bucket=bucket_name)
       elif action == 'upload':
           s3.upload_file(file_path, bucket_name)

3. CloudWatch Metrics:
   def get_metric_stats(
       namespace: str,
       metric_name: str,
       dimensions: List[Dict]
   ) -> Dict[str, Any]:
       return cloudwatch.get_metric_statistics(
           Namespace=namespace,
           MetricName=metric_name,
           Dimensions=dimensions,
           StartTime=datetime.now() - timedelta(hours=1),
           EndTime=datetime.now(),
           Period=300,
           Statistics=['Average']
       )

4. Resource Tagging:
   def tag_resource(
       resource_id: str,
       tags: List[Dict[str, str]]
   ):
       ec2.create_tags(
           Resources=[resource_id],
           Tags=tags
       )

Bonus Challenges:
1. Implement auto-scaling
2. Create backup system
3. Add cost optimization
4. Build disaster recovery

Tips:
- Use IAM roles
- Implement retry logic
- Add error handling
- Monitor costs
- Use resource tagging
"""

import boto3
from typing import List, Dict, Any
import json
from datetime import datetime, timedelta

class AWSManager:
    """
    Your Task:
    1. Initialize AWS clients with proper error handling for credentials
    2. Implement methods to manage EC2 instances
    3. Add S3 bucket operations
    4. Create CloudWatch metrics monitoring
    
    Requirements:
    - Handle AWS credentials properly
    - Implement proper error handling for AWS API calls
    - Add rate limiting for API requests
    - Document the methods with proper docstrings
    """
    def __init__(self, region: str):
        """
        TODO: Initialize the AWS manager with:
        - Proper credentials handling
        - Client initialization
        - Error handling
        """
        self.session = boto3.Session()
        self.region = region
        self.ec2 = self.session.resource('ec2', region_name=region)
        self.s3 = self.session.resource('s3', region_name=region)
        self.cloudwatch = self.session.client('cloudwatch', region_name=region)
    
    def list_instances(self) -> List[Dict[str, Any]]:
        """
        TODO: Implement EC2 instance listing
        - List all EC2 instances in the region
        - Include instance details (state, type, tags)
        - Handle pagination for large lists
        """
        instances = self.ec2.instances.all()
        instance_list = []
        for instance in instances:
            instance_list.append({
                'id': instance.id,
                'state': instance.state['Name'],
                'type': instance.instance_type,
                'tags': instance.tags
            })
        return instance_list
    
    def get_instance_metrics(self, instance_id: str) -> Dict[str, Any]:
        """
        TODO: Implement CloudWatch metrics retrieval
        - Get CPU, memory, and network metrics
        - Handle time ranges and statistics
        - Implement proper error handling
        """
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=1)
        
        metrics = {
            'CPU': self.cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=start_time,
                EndTime=end_time,
                Period=300,
                Statistics=['Average']
            ),
            'Network': self.cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='NetworkIn',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=start_time,
                EndTime=end_time,
                Period=300,
                Statistics=['Average']
            )
        }
        
        return metrics
    
    def manage_s3_bucket(self, bucket_name: str, action: str, file_path: str = None):
        """
        TODO: Implement S3 bucket operations
        - Create/delete buckets
        - List bucket contents
        - Handle bucket policies
        - Implement proper error handling
        """
        if action == 'create':
            self.s3.create_bucket(Bucket=bucket_name)
        elif action == 'delete':
            self.s3.Bucket(bucket_name).delete()
        elif action == 'upload' and file_path:
            self.s3.Bucket(bucket_name).upload_file(file_path, file_path.split('/')[-1])
        elif action == 'list':
            return [obj.key for obj in self.s3.Bucket(bucket_name).objects.all()]
    
    def launch_instance(
        self,
        image_id: str,
        instance_type: str,
        key_name: str,
        security_groups: List[str]
    ) -> Dict[str, Any]:
        """
        Launch an EC2 instance.

        :param image_id: ID of the AMI
        :param instance_type: Type of the instance (e.g., 't2.micro')
        :param key_name: Name of the key pair
        :param security_groups: List of security group IDs or names
        :return: Response from the EC2 run_instances call
        """
        return self.ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_groups,
            MinCount=1,
            MaxCount=1
        )
    
    def get_metric_stats(
        self,
        namespace: str,
        metric_name: str,
        dimensions: List[Dict]
    ) -> Dict[str, Any]:
        """
        Get CloudWatch metric statistics.

        :param namespace: Namespace of the metric
        :param metric_name: Name of the metric
        :param dimensions: List of dimensions for the metric
        :return: Metric statistics
        """
        return self.cloudwatch.get_metric_statistics(
            Namespace=namespace,
            MetricName=metric_name,
            Dimensions=dimensions,
            StartTime=datetime.now() - timedelta(hours=1),
            EndTime=datetime.now(),
            Period=300,
            Statistics=['Average']
        )
    
    def tag_resource(
        self,
        resource_id: str,
        tags: List[Dict[str, str]]
    ):
        """
        Tag an AWS resource.

        :param resource_id: ID of the resource (e.g., EC2 instance ID)
        :param tags: List of tags to add to the resource
        """
        self.ec2.create_tags(
            Resources=[resource_id],
            Tags=tags
        )

def main():
    # TODO: Implement main function to demonstrate AWS operations
    pass

if __name__ == "__main__":
    main()
