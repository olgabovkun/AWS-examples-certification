# Example of creating STS
AWS Security Token Service (STS) action that allows one role or user to temporarily assume the permissions of another IAM role.

## Init
cd api/sts
chmod +x bin/deploy

## Create a user with no permissions

Creates a new IAM user:
```sh
aws iam create-user --user-name sts-test-user
```

Create secret access key and corresponding AWS access key ID for the specified user:
```sh
aws iam create-access-key --user-name sts-test-user --output table
```

Copy the AccessKeyId and SecretAccessKey:
```sh
aws configure
```

Update credentials file with new 'sts' profile instead of 'default'
```sh
open ~/.aws/credentials
```

Check identity:
```sh
aws sts get-caller-identity --profile sts
```

Check that this user don't have any permission:
```sh
aws s3 ls s3://sts-example-56289 --profile sts
```
> An error occurred (AccessDenied) when calling the ListBuckets operation

## Create a Role

Execute deploy to create IAM Role with s3access
```sh
./bin/deploy
```

## Use new user credentials and assume role

Attach inline policy to the user to allow us to assume that specific role
```sh
aws iam put-user-policy \
--user-name sts-test-user \
--policy-name StsAssumePolicy \
--policy-document file://policy.json
```

Assume role. It should return credentials
```sh
aws sts assume-role \
--role-arn arn:aws:iam::429987468922:role/my-sts-stack-StsRole-842hrM4KLMAT \
--role-session-name sts-example-s3 \
--profile sts
```
> output:
<!-- {
    "Credentials": {
        "AccessKeyId": "EXAMPLEACCESSKEYID",
        "SecretAccessKey": "EXAMPLESECRETACCESSKEY",
        "SessionToken": "EXAMPLESESSIONTOKEN",
        "Expiration": "2024-08-25T02:59:01+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "ASSUMEDROLEIDEXAMPLE",
        "Arn": "ARNIAMROLE"
    }
} -->

Update aws configuration file and add new 'assumed' profile with new aws_access_key_id, aws_secret_access_key, aws_session_token
Update credentials file with new 'sts' profile instead of 'default'
```sh
open ~/.aws/credentials
```
<!-- 
[assumed]
aws_access_key_id = EXAMPLEACCESSKEYID
aws_secret_access_key = EXAMPLESECRETACCESSKEY/bu0iXfSFePzLy
aws_session_token = EXAMPLESESSIONTOKEN
-->

Check assumed sts identity. Arn should have '/role-session-name' that we defined before
```sh
aws sts get-caller-identity --profile assumed
```

## Test
For 'sts' profile it should return AccessDenied
```sh
aws s3 ls s3://sts-example-56289 --profile sts
```

For the 'assumed' profile, it should work. 
Get objects from the S3 --bucket sts-example-56289. The bucket is empty since we haven’t added anything yet, but you can manually upload a file through the AWS Console to test it
```sh
aws s3 ls s3://sts-example-56289 --profile assumed
```

## Cleanup
Delete Cloudformation stack:
```sh
aws cloudformation delete-stack --stack-name my-sts-stack
```

Delete user policy:
```sh
aws iam delete-user-policy \
--user-name sts-test-user \
--policy-name StsAssumePolicy
```

Delete access key:
To delete access key we need to open credential file and copy access_key for 'sts' profile:
```sh
open ~/.aws/credentials

```
Copy your access_key and paste for tag --access-key-id
```sh
aws iam delete-access-key \
--access-key-id EXAMPLEACCESSKEYID \
--user-name sts-test-user
```

Delete user:
```sh
aws iam delete-user --user-name sts-test-user
```

As the last step, if you are working locally, delete the .aws credentials file. If you are working through gitpod, it will be deleted automatically after stopping the workspace