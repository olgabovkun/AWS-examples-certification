## Create Lambda
Here’s an example of how to create a simple AWS Lambda function using SAM. The function will be written in Python and deployed using inline code.

## Init
```sh
cd lambda/create-function/sam/
```

## Install sam cli
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

For linux-x86_64:
```sh
chmod +x aws_sam_cli_install.sh
./aws_sam_cli_install.sh
```

## SAM build
```sh
sam build
```

## SAM deploy
```sh
chmod +x deploy
./deploy
```

## Cleanup
#### Delete Cloudformation stack for lambda
```sh
aws cloudformation delete-stack \
--stack-name sam-python-lambda-function-stack
```