
# How to use deploy.py

The `deploy.py` script contains functions for deploying a project to an Amazon Elastic Compute Cloud (EC2) instance. To use the script, you will need to have an EC2 instance set up and have the necessary credentials for accessing it.

## Prerequisites

-   An EC2 instance
-   Access to the AWS Management Console
-   AWS Access Key ID and Secret Access Key
-   Git and pip installed on the local machine

## Setting up the environment

1.  Clone the project repository to your local machine.

`git clone https://github.com/your-username/your-project.git` 

2.  Navigate to the project directory.

`cd your-project` 

3.  Install the required packages.

`pip install -r requirements.txt` 

## Deploying the project

1.  Import the `EC2` class from the `deploy` script.

`from deploy import EC2` 

2.  Create an `EC2` object and pass in the necessary parameters:

-   `access_key_id`: Your AWS Access Key ID
-   `secret_access_key`: Your AWS Secret Access Key
-   `region_name`: The region where your EC2 instance is located
-   `instance_id`: The ID of your EC2 instance

`ec2 = EC2(access_key_id, secret_access_key, region_name, instance_id)` 

3.  Use the `deploy` method to deploy the project to the EC2 instance.

`ec2.deploy()` 

The `deploy` method will perform the following actions:

-   Connect to the EC2 instance using SSH
-   Pull the latest code from the repository
-   Install the required packages using pip
-   Restart the server to apply the changes

## Additional functions

In addition to the `deploy` method, the `EC2` class also provides the following functions:

-   `run_command`: Run a command on the EC2 instance
-   `put_file`: Transfer a file from the local machine to the EC2 instance
-   `get_file`: Transfer a file from the EC2 instance to the local machine

## Example usage

Here is an example of how to use the `run_command` function to navigate to the project directory, install the required packages, and start the server:

`commands = [
    "cd path/to/project/directory",
    "pip install -r requirements.txt",
    "python3 main.py"
]
ec2.run_command(commands)`
