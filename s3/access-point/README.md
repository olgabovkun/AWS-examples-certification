# Access Point
In this example we are going to create bucket and access point using AWS CLI

## Init
```sh
cd s3/access-point/
export BUCKET_NAME=my-test-access-point-bucket
export REGION=us-west-2
export ACCOUNT_ID=<your-account-id>
export ACCESS_POINT_NAME=my-access-point
export USER_NAME=<your-user-name>
```

## Create bucket
```sh
aws s3api create-bucket \
--bucket $BUCKET_NAME \
--region $REGION \
--create-bucket-configuration LocationConstraint=$REGION
```

If you getting exception `An error occurred (BucketAlreadyExists)` create a new bucket name.

## Create Access Point 
Creating an S3 Access Point associated with this bucket. This access point will provide controlled access to the data in the bucket:
```sh
ACCESS_POINT_ARN=$(aws s3control create-access-point \
--account-id $ACCOUNT_ID \
--bucket $BUCKET_NAME \
--name $ACCESS_POINT_NAME \
--region $REGION \
--query 'AccessPoint.Arn' \
--output text)
```

## Upload a Test File to the Bucket
Before uploading, let's create a test file locally:
```sh
echo "This is a test file" > testfile.txt
```

Upload the file created earlier to the bucket:
```sh
aws s3 cp testfile.txt s3://$BUCKET_NAME/testfile.txt
```

## Set Permissions for the Access Point
Associates an access policy with the specified access point:
```sh
aws s3control put-access-point-policy \
--account-id $ACCOUNT_ID \
--name $ACCESS_POINT_NAME \
--policy "$(cat <<EOF 
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
               "AWS": "arn:aws:iam::$ACCOUNT_ID:user/$USER_NAME"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:$REGION:$ACCOUNT_ID:accesspoint/$ACCESS_POINT_NAME/object/*"
        }
    ]
}
EOF
)"
```

## Test
### Access the File Through the Access Point:
Use the access point to get the object. If the command is successful, it confirms you have access through the access point:
```sh
aws s3api get-object \
--bucket arn:aws:s3:$REGION:$ACCOUNT_ID:accesspoint/$ACCESS_POINT_NAME \
--key testfile.txt downloaded-file.txt
```

Verify the Downloaded File:
```sh
cat downloaded-file.txt
```

## Modify the Access Point Policy
To test denied access, you can change the policy to restrict access:
```sh
aws s3control put-access-point-policy \
--account-id $ACCOUNT_ID \
--name $ACCESS_POINT_NAME \
--policy "$(cat <<EOF 
{
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": {
               "AWS": "arn:aws:iam::$ACCOUNT_ID:user/$USER_NAME"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:$REGION:$ACCOUNT_ID:accesspoint/$ACCESS_POINT_NAME/object/*"
        }
    ]
}
EOF
)"
```

## Test
Attempt to access the file through the access point again. This time, you should receive an error indicating that access is denied:
```sh
aws s3api get-object \
--bucket arn:aws:s3:$REGION:$ACCOUNT_ID:accesspoint/$ACCESS_POINT_NAME \
--key testfile.txt downloaded-file.txt
```

Verify the Downloaded File:
```sh
cat downloaded-file.txt
```

## Clean up
#### Delete the object from the bucket
```sh
aws s3api delete-object \
--bucket $BUCKET_NAME \
--key testfile.txt
```
#### Delete the access point
```sh
aws s3control delete-access-point \
--account-id $ACCOUNT_ID \
--name $ACCESS_POINT_NAME
```

#### Delete the S3 bucket
```sh
aws s3api delete-bucket \
--bucket $BUCKET_NAME \
--region $REGION
```

#### Remove the local file
```sh
rm testfile.txt downloaded-file.txt
```

#### Unset the variable
```sh
unset BUCKET_NAME
unset REGION
unset ACCOUNT_ID
unset ACCESS_POINT_NAME
unset USER_NAME
```