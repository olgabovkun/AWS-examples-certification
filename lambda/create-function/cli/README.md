# Create Lambda
Here’s an example of how to create a simple AWS Lambda function using AWS CLI. The function will be written in Python and deployed from a local file.

> You can run the step-by-step commands or use a bash script for creating and deleting a Lambda function (before running the script, ensure that it has executable permissions)
> 
> ./create-lambda
> 
> ./delete-lambda

## Init
```
cd lambda/create-function/cli
```

## Create a Role for Lambda
First, you need to create an IAM role with the appropriate permissions for Lambda function.
```sh
aws iam create-role \
--role-name lambda-execution-role \
--assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }]
  }' \
--query 'Role.Arn' \
--output text
```

Copy ARN output and use replace later instead of <role-arn>

## Attach the AWSLambdaBasicExecutionRole policy
Attach the AWSLambdaBasicExecutionRole policy to this role to allow logging (otherwise we won't have any logs for lambda):
```sh
aws iam attach-role-policy \
--role-name lambda-execution-role \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

## Create a Deployment Package
Zip the Python file into a deployment package:
```sh
zip function.zip ../lambda-function.py
```

## Create the Lambda Function
Use the AWS CLI to create the Lambda function. Replace <role-arn> with the ARN of the role created earlier:
```sh
aws lambda create-function \
--function-name python-lambda-function \
--zip-file fileb://function.zip \
--handler lambda-function.handler \
--runtime python3.9 \
--role <role-arn>
```

AWS Lambda automatically creates a log group in CloudWatch Logs. The log group name follows the format /aws/lambda/<function-name>. 

## Test
Invoke the Lambda function using the following command:
```sh
aws lambda invoke \
--function-name python-lambda-function \
output.txt
```

Check the output of the Lambda function:
```sh
cat output.txt
```

## Cleanup
#### Delete the Lambda function
```sh
aws lambda delete-function \
--function-name python-lambda-function
```

#### Delete IAM role
AWS IAM requires you to detach all policies from a role before you can delete the role.

First, check which policies are attached to the role. This command will return a list of attached policies. Copy <PolicyArn>.
```sh
aws iam list-attached-role-policies \
--role-name lambda-execution-role
```

For each attached policy, detach it using its ARN. Replace <policy-arn> with the actual ARN of the policy:
```sh
aws iam detach-role-policy \
--role-name lambda-execution-role \
--policy-arn <policy-arn>
# it should be the same as we attached before `arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole`
```

Delete role:
```sh
aws iam delete-role \
--role-name lambda-execution-role
```

#### Delete a log group
```sh
aws logs delete-log-group \
--log-group-name /aws/lambda/python-lambda-function
```

#### Delete generated zip file and output
```sh
rm function.zip
```

```sh
rm output.txt
```
