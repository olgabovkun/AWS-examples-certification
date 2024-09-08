# AWS-examples-certification

This repository contains various AWS code examples to help prepare for AWS Solutions Architect Associate Certification (SAA-C03).

## Gitpod
https://www.gitpod.io/docs/introduction/getting-started

You can work with this repository using Gitpod as the cloud-based development environment.
The .gitpod file contains the necessary tools that will be installed before starting development in Gitpod

## Configuring AWS Credentials

* **Using Gitpod** - Before starting to work with the scripts mentioned in this repository, you need to set up the following AWS environment variables:
    ```sh
    gp env AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID 
    gp env AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
    gp env AWS_DEFAULT_REGION=us-west-2
    ```
* **Locally** - use one of the following options:
    * Use AWS CLI. Run the Configuration Command. Follow the prompts to enter your AWS access key ID, secret access key and region
      ```sh
      aws configure
      ```
    * Use Environment Variables
      ```sh
      export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
      export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
      export AWS_DEFAULT_REGION=us-west-2
      ```

## Bash scripts
Before running the script, ensure that it has executable permissions:
```
chmod +x script_name.sh
```
