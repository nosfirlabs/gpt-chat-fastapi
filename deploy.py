import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get the ID of the EC2 instance you want to deploy to
instance_id = ''

# Run the following command on the EC2 instance
# git clone https://github.com/nosfirlabs/gpt-chat-fastapi.git
response = ec2.run_command(
    InstanceIds=[instance_id],
    DocumentName='AWS-RunShellScript',
    Parameters={
        'commands': [
            'git clone https://github.com/nosfirlabs/gpt-chat-fastapi.git',
            'cd gpt-chat-fastapi',
            'pip install -r requirements.txt',
            'python3 main.py'
        ]
    }
)
print(response)
