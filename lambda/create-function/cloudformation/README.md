# Create Lambda
Here’s an example of how to create a simple AWS Lambda function using AWS CloudFormation. The function will be written in Python and deployed using inline code.

## Init
```sh
cd lambda/create-function/cloudformation
chmod +x deploy
```

## Deploy. Create lambda function 
Execute deploy to create lambda function `python-lambda-function` and IAM role with the appropriate permissions for Lambda. 

AWS Lambda automatically creates a log group in CloudWatch Logs. The log group name follows the format /aws/lambda/<function-name>. 

```sh
./deploy
```

## Cleanup
#### Delete Cloudformation stack for lambda
```sh
aws cloudformation delete-stack \
--stack-name python-lambda-function-stack
```

#### Delete a log group
```sh
aws logs delete-log-group \
--log-group-name /aws/lambda/python-lambda-function
```