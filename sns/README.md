# Create a topic
In this example we are going to create simple SNS topic `MySNSTopic` using cli and CloudFormation
<!-- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html -->

## Init
```sh
cd sns
chmod +x deploy
```

## Create SNS topic 
* Create `MySNSTopicCF` SNS topic with CF:
```sh
./deploy
```

* Create `MySNSTopicCLI` SNS topic with CLI:
```sh
aws sns create-topic \
--name MySNSTopicCLI
```

## Cleanup
* Delete Cloudformation stack:
```sh
aws cloudformation delete-stack --stack-name my-sns-stack
```

* Delete CLI created topic. Replace topic-arn with yours
```sh
aws sns delete-topic \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic"
```