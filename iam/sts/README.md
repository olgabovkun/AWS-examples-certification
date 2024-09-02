# AWS STS (Security Token Service)

```sh
aws sts get-caller-identity
```

# Steps for Assuming a Role
 
## Create IAM User
```sh
aws iam create-user 
--user-name StsExampleUser
```

## Check user has no permissions
```sh
aws s3 ls
```

## Create IAM Role with a trust relation with the created IAM User
#### Trust Policy Document is saved as trust-policy.json. This policy allows the user StsExampleUser to assume the role.
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
```sh
aws iam put-user-policy \
--user-name StsExampleUser \
--policy-name AssumeRolePolicy \
--policy-document file://assume-role-policy.json
```

## Check list of attached policies
```sh
aws iam list-attached-role-policies --role-name StsExampleRole
```
```sh
aws iam list-attached-user-policies \
--user-name StsExampleUser
```

## Create access key for this user
```sh
aws iam create-access-key --user-name StsExampleUser
```

## AWS configure
```sh
aws configure --profile sts-example
```

## Check identity
```sh
aws sts get-caller-identity 
```

## Assume role
```sh
aws sts assume-role \
--role-arn arn:aws:iam::123456789012:role/StsExampleRole \
--role-session-name StsExampleSession
```

## Verify Access to S3
```sh
aws s3 ls --profile sts-example
```