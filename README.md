📌 Event-Driven DevOps Automation Pipeline on AWS
📖 Project Overview

1. This project demonstrates an event-driven DevOps automation pipeline built on AWS.
2. It automates container deployment, monitoring, and alerting using multiple cloud services.
3. The system uses Docker containers, AWS messaging services, and serverless automation to create a scalable deployment workflow.

==============================================================================

🏗 Architecture:-
The workflow of the system is:-

Developer Push Code
        ↓
Docker Build
        ↓
Application stored in S3
        ↓
Event Trigger
        ↓
SQS Queue receives message
        ↓
Lambda processes event
        ↓
SNS sends deployment notification

==============================================================================

☁️ AWS Services Used

| Service | Purpose                  |
| ------- | ------------------------ |
| EC2     | Application hosting      |
| S3      | Artifact storage         |
| VPC     | Secure networking        |
| SNS     | Notification service     |
| SQS     | Message queue            |
| Lambda  | Event processing         |
| AMI     | Golden image for scaling |

==============================================================================

🐳 Tools & Technologies

1. Docker
2. Bash Scripting
3. AWS CLI
4. Python (Lambda)
5. Git
6. GitHub

==============================================================================

⚙️ Features

✔ Event-driven architecture
✔ Containerized application deployment
✔ Automated alerting system
✔ Serverless processing with Lambda
✔ Infrastructure ready for scaling with AMI

==============================================================================

📂 Project Structure

P01/
│
├── Event-Driven_DevOps_Automation_Pipeline_on_AWS
│   ├── Docker/
│   │   └── docker-image-tarfile
|   |   └── dockerfile
|   |   └── index.html   
│   │
│   ├── Lambda/
│   │   └── lambda_function.py
│   │
│   ├── Scripts/
│   │   └── deploy.sh
│   │   └── install_docker.sh
│   │
│   └── README.md

=============================================================================
