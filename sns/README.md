# Create a topic
In this example we are going to create Standard SNS topic `MySNSTopic` using cli and CloudFormation
<!-- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html -->

## Init
```sh
cd sns
chmod +x deploy
```

## Create SNS topic 
* Create Standard `MySNSTopicCF` SNS topic with CF:
```sh
./deploy
```

* Create Standard `MySNSTopicCLI` SNS topic with CLI:
```sh
aws sns create-topic \
--name MySNSTopicCLI
```

* Create FIFO `MySNSTopicFIFO` SNS topic with CLI. For a FIFO topic, the name must end with the .fifo suffix:</br>
`ContentBasedDeduplication` is an attribute of Amazon SNS FIFO topics that helps prevent the delivery of duplicate messages.</br>
How It Works:</br>
* **When Enabled**: SNS uses a SHA-256 hash of the message body to identify duplicate messages. If a message with the same body is published within a 5-minute deduplication interval, SNS considers it a duplicate and does not deliver it again.
* **When Disabled** (default): You must provide a MessageDeduplicationId for each message. This ID is used to identify duplicates and ensure that messages are not processed more than once.

```sh
aws sns create-topic \
--name MySNSTopicCLI.fifo \
--attributes FifoTopic=true,ContentBasedDeduplication=true
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