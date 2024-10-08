# API Gateway
Here’s an example of setting up an AWS API Gateway and testing it using the AWS CLI.

## Create a REST API
```sh
aws apigateway create-rest-api \
--name "TestAPI" \
--description "API for testing purposes"
```

Copy `id` and `rootResourceId` from the response.

## Create Resource
Replace <api-id> with the API ID from the previous command, and <root-resource-id> with the root resource ID of your API. This will create a new resource /test.

```sh
aws apigateway create-resource \
--rest-api-id <api-id> \
--parent-id <root-resource-id> \
--path-part "test"
```

Copy `id` from the response:

## Create a GET Method for the Resource
Replace <api-id> and <resource-id> from the previous step
```sh
aws apigateway put-method \
--rest-api-id <api-id> \
--resource-id <resource-id> \
--http-method GET \
--authorization-type NONE
```

## Create Lambda
for integration we need to create a Lambda function first:
```sh
cd ../lambda/create-function/cli/ # navigate to this folder /lambda/create-function/cli
chmod +x created-lambda
./create-lambda
```

## Add permissions
We should add a resource-based policy that grants API Gateway permission to invoke your Lambda function:
```sh
aws lambda add-permission \
--function-name python-lambda-function \
--principal apigateway.amazonaws.com \
--statement-id AllowAPIGatewayInvoke \
--action lambda:InvokeFunction
```

## Integrate the Method with a Lambda
Replace <api-id> and <resource-id> from the previous step; update `uri` with <region> and <function-arn>:
```sh
aws apigateway put-integration \
--rest-api-id <api-id> \
--resource-id <resource-id> \
--http-method GET \
--type AWS_PROXY \
--integration-http-method POST \
--uri "arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/<lambda-function-arn>/invocations"
```

## Deploy API
Replace <api-id>:
```sh
aws apigateway create-deployment \
--rest-api-id <api-id> \
--stage-name dev
```

## Test API
Test API, you should see the response from lambda function: "Check CloudWatch Logs for the message!"

Replace <api-id> and <region>:
```sh
curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/dev/test
```

# Clean up
## Delete API Gateway
Replace <api-id>: 
```sh
aws apigateway delete-rest-api \
--rest-api-id <api-id>
```

## Delete Lambda
```sh
cd ../lambda/create-function/cli/
chmod +x delete-lambda
./delete-lambda
```