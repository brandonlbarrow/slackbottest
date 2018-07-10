import boto3

class SlackyBotEC2:

    def __init__(self, aws_config_profile):
        aws_session = boto3.session.Session(
            profile_name=aws_config_profile
        )
        self.ec2 = aws_session.client('ec2')
    
    def get_running_instances(self):
        return self.ec2.describe_instances()
