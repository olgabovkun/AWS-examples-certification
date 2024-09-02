# STS get identity

```sh
aws sts get-caller-identity
```
Output:
```
{
    "UserId": "AIDASAMPLEUSERID",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/DevAdmin"
}
```

# Steps for Assuming a Role
 
## Go to sts directory
```sh
cd iam/sts/
```

## Create IAM User
```sh
aws iam create-user \
--user-name StsExampleUser
```
Output:
```
{
    "User": {
        "UserName": "Bob",
        "Path": "/",
        "CreateDate": "2023-06-08T03:20:41.270Z",
        "UserId": "AIDAIOSFODNN7EXAMPLE",
        "Arn": "arn:aws:iam::123456789012:user/Bob"
    }
}
```

Copy ARN from output

## Create access key for this user
```sh
aws iam create-access-key --user-name StsExampleUser
```
Output:
```
{
    "AccessKey": {
        "UserName": "Bob",
        "Status": "Active",
        "CreateDate": "2015-03-09T18:39:23.411Z",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY",
        "AccessKeyId": "AKIAIOSFODNN7EXAMPLE"
    }
}
```

Copy AccessKeyId and SecretAccessKey from output

## AWS configure
```sh
aws configure --profile sts-example
```
Insert created AccessKeyId and SecretAccessKey

## Check identity
```sh
aws sts get-caller-identity --profile sts-example
```

## Check user has no permissions
```sh
aws s3 ls --profile sts-example
```

Expected Output:
```
An error occurred (AccessDenied) when calling the ListBuckets operation: User: arn:aws:iam::123456789012:user/Bob is not authorized to perform: s3:ListAllMyBuckets because no identity-based policy allows the s3:ListAllMyBuckets action
```

## Create IAM Role with a trust relation with the created IAM User
Trust Policy Document is saved as trust-policy.json. This policy allows the user StsExampleUser to assume the role.

Update trust-policy.json with ARN for created User or use cli command: 
```sh
aws iam get-user --user-name StsExampleUser
```

Create Role with trust relation policy
```sh
aws iam create-role \
--role-name StsExampleRole \
--assume-role-policy-document file://trust-policy.json
```

## Attach S3 Policy to the Role
```sh
aws iam put-role-policy \
--role-name StsExampleRole \
--policy-name S3ListRolePolicy \
--policy-document file://s3-policy.json
```

## Attach assume-role-policy to the User

Update assume-role-policy.json with ARN for created Role or use cli command: 
```sh
aws iam get-role \
--role-name StsExampleRole
```

Add AssumeRole policy to the user
```sh
aws iam put-user-policy \
--user-name StsExampleUser \
--policy-name AssumeRolePolicy \
--policy-document file://assume-role-policy.json
```

<!-- ## Check list of attached policies
```sh
aws iam list-attached-role-policies \
--role-name StsExampleRole
```
```sh
aws iam list-attached-user-policies \
--user-name StsExampleUser
``` -->

## Assume role
Update role-arn with the ARN for created Role
```sh
aws sts assume-role \
--profile sts-example \
--role-arn arn:aws:iam::429987468922:role/StsExampleRole \
--role-session-name StsExampleSession
```

## Configure profile with temperarly credentials
Update sts-example profile and insert session token
```sh
nano ~/.aws/config
nano ~/.aws/credentials
```

## Verify Access to S3
```sh
aws s3 ls --profile sts-example
```