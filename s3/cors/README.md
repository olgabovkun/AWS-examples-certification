# Test POST Request with CORS 

## Init
cd s3/cors/

## Create bucket

```sh
aws s3 mb s3://cors-fun-testbucket123
```

## Change block public access

```sh
aws s3api put-public-access-block \
--bucket cors-fun-testbucket123 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

## Create bucket policy

```sh
aws s3api put-bucket-policy \
--bucket cors-fun-testbucket123 \
--policy file://policy.json
```

## Turn on static website hosting

```sh
aws s3api put-bucket-website \
--bucket cors-fun-testbucket123 \
--website-configuration file://website.json
```

## Upload our index.html file and include resource that would be cross-origin

```sh
aws s3 cp index.html s3://cors-fun-testbucket123
```

## View website
### The format for the website endpoint: http://bucket-name.s3-website-region.amazonaws.com

http://cors-fun-testbucket123.s3-website-us-west-2.amazonaws.com


## Create API gateway with POST to test CORS

### create a new API
```sh
aws apigateway create-rest-api \
--name "HelloWorldAPI" \
--description "API that returns 'hello world'" \
--query "id" \
--output text
```
save returned API_ID: 1iwfuvmozk

### Get the root resource ID for your API:
```sh
aws apigateway get-resources \
--rest-api-id 1iwfuvmozk \
--query "items[?path=='/'].id" \
--output text
```
save returned ROOT_RESOURCE_ID: u2408s7vj8

### Create a new resource under the root resource:
```sh
aws apigateway create-resource \
--rest-api-id 1iwfuvmozk \
--parent-id u2408s7vj8 \
--path-part "hello" \
--query "id" \
--output text
```
save returned RESOURCE_ID: maxx48

### Create a POST method for the newly created resource:
```sh
aws apigateway put-method \
--rest-api-id 1iwfuvmozk \
--resource-id maxx48 \
--http-method POST \
--authorization-type NONE
```

### Create a mock integration for the POST method:
```sh
aws apigateway put-integration \
--rest-api-id 1iwfuvmozk \
--resource-id maxx48 \
--http-method POST \
--type MOCK \
--request-templates '{"application/json": "{\"statusCode\": 200}"}'
```

### Set up the mock integration response to return "hello world":
```sh
aws apigateway put-method-response \
--rest-api-id 1iwfuvmozk \
--resource-id maxx48 \
--http-method POST \
--status-code 200 \
--response-models '{"application/json": "Empty"}'
```
```sh
aws apigateway put-integration-response \
--rest-api-id 1iwfuvmozk \
--resource-id maxx48 \
--http-method POST \
--status-code 200 \
--selection-pattern "" \
--response-templates '{"application/json": "{\"message\": \"hello world\"}"}'
```

### Create a new deployment stage:
```sh
aws apigateway create-deployment \
--rest-api-id 1iwfuvmozk \
--stage-name dev
```

### Test endpoint
```sh
aws apigateway get-stage \
--rest-api-id 1iwfuvmozk \
--stage-name dev \
--query "invokeUrl" \
--output text
```

### CURL to test
curl -X POST https://1iwfuvmozk.execute-api.us-west-2.amazonaws.com/dev/hello

## Apply CORS policy

### apply CORS to s3
```sh
aws s3api put-bucket-cors \
--bucket cors-fun-testbucket123 \
--cors-configuration file://cors.json
```
### apply CORS on api gateway
through AWS console on /hello method
then deploy

## Clean up
### Delete the Deployment Stage
```sh
aws apigateway delete-stage \
--rest-api-id 1iwfuvmozk \
--stage-name dev
```

### Delete the API
```sh
aws apigateway delete-rest-api --rest-api-id 1iwfuvmozk
```

### Verify Deletion API
```sh
aws apigateway get-rest-apis
```

### Remove bucket
```sh
../crud-bucket-object/delete-objects cors-fun-testbucket123
```
```sh
../crud-bucket-object/delete-bucket cors-fun-testbucket123
```