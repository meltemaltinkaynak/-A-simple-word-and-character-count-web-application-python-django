AWS deployment
1. Creating ec2 instance and key pair in AWS
2. Connecting to your EC2 instance via Putty
3. Under the Cloud Project file, we created a virtual environment named myproject env and
activated it.
4. We updated pip in the virtual environment
5. We installed Django and the necessary packages
6. We copied your project to ec2 instance as .zip
7. Unzip our project with the unzip command
8. We installed the required Python packages using the requirements.txt file containing the
requirements for your Django project
9. We edited the settings.py file using the nano text editor. We added the Public IPv4 DNS and
Public IPv4 address that the server can access to the ALLOWED_HOSTS list
10. We started the Django server and ran it on port 0.0.0.0:8000
