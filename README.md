# Docker-prose-
Headline: 🐳 My Journey from Local Code to AWS Cloud with Docker

I just successfully deployed a containerized Python application on an AWS EC2 instance! This project helped me bridge the gap between software development and cloud infrastructure.

How I did it (Step-by-Step):

1️⃣ Setting up the AWS Infrastructure:

Launched an EC2 Instance (Amazon Linux).

Configured Security Groups to allow inbound traffic on Port 5000.

Installed Docker: sudo yum install docker -y && sudo systemctl start docker.

2️⃣ Developing the Container:

Wrote a Dockerfile to package my Python Flask app and its dependencies.

Learned the importance of binding the host to 0.0.0.0 for cloud accessibility.

3️⃣ Deployment Commands: If you want to test my project on your own server, here are the exact commands:

Bash

# Clone the repository
git clone https://github.com/sperigisetty1-ship-it/Docker-prose-.git
cd Docker-prose-

# Build the Docker image
docker build -t python-app .

# Run the container in detached mode
docker run -d -p 5000:5000 python-app
📍 The Result: The app is live! By visiting the EC2 Public IP on port 5000, I can see my application running smoothly in its isolated environment.

Key Learnings:

Isolation: Docker ensures the app runs the same on EC2 as it does on my laptop.

Troubleshooting: Used docker logs and docker ps -a to debug initial container crashes.

Security: Understanding how Cloud Firewalls (Security Groups) protect and expose our services.
