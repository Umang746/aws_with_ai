# AWS with AI - Finger Count-based EC2 Instance Launcher

![AWS](https://img.shields.io/badge/AWS-Amazon%20Web%20Services-yellow?style=for-the-badge&logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)

This project leverages Python and its libraries to connect with AWS and dynamically launch EC2 instances based on the user's live input of finger count.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Overview

AWS with AI is an innovative project that combines the power of Amazon Web Services (AWS) with artificial intelligence to dynamically launch EC2 instances based on real-time finger count input. The project utilizes Python and computer vision libraries to recognize the number of fingers a user is showing through a live camera feed. Subsequently, it triggers the launch of the corresponding number of EC2 instances on AWS.

## Features

- **Finger Count Recognition:** Leverages computer vision to accurately count the number of fingers displayed by the user.
  
- **Dynamic EC2 Launch:** Instantly launches EC2 instances on AWS based on the recognized finger count, providing a seamless and responsive experience.

- **AWS Integration:** Utilizes the AWS SDK for Python (Boto3) to establish a secure connection with AWS and automate the EC2 instance provisioning process.

- **User-Friendly Interface:** Simple on-screen instructions guide users through the process, making it accessible for users with varying technical backgrounds.

## Demo

**Run the Demo Locally:**

   - Ensure you have followed the [Installation](#installation) instructions.
   - Run the application:

     ```bash
     python main.py
     ```

   - Follow on-screen instructions to provide live finger count input and witness the corresponding launch of EC2 instances.

## Prerequisites

Before using this project, ensure you have the following prerequisites:

- Python 3.x installed
- AWS account with necessary credentials configured
- Libraries mentioned in `requirements.txt` installed

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Umang746/aws_with_ai.git
    cd aws_with_ai
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Follow on-screen instructions to provide live finger count input and launch corresponding EC2 instances.

