# Create a subscription to the topic
In this example, we will create an SNS topic and a subscription to it via Email, and then try to publish a message using the CLI.

## Create Standard SNS topic
```sh
aws sns create-topic \
--name MySNSTopicSubEmail
```

## Create Subscription
To test the subscription, we will use the Email protocol.

Replace `topic-arn` with your topic's ARN and `your-email@example.com` with the email address you want to subscribe:
```sh
aws sns subscribe \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
--protocol email \
--notification-endpoint "your-email@example.com"
```

## Confirm Subscription
* **Check Your Email**: You will receive an email from AWS SNS containing a confirmation link
* **Confirm Subscription**: Click the confirmation link in the email to complete the subscription process

## Test
Publish a message to your SNS topic:
```sh
aws sns publish \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
--message "This is a test message"
```
Check your email to view the incoming requests and messages.

## Cleanup
#### List Subscriptions
First, list all subscriptions to get the Subscription ARNs:
```sh
aws sns list-subscriptions
```

#### Delete Subscription
Use the Subscription ARNs obtained from the previous step:
```sh
aws sns unsubscribe \
--subscription-arn arn:aws:sns:us-west-2:0123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f
```

#### List Topics
List all topics to get the Topic ARNs:
```sh
aws sns list-topics
```

#### Delete CLI created topic:
Replace topic-arn with your topic's ARN
```sh
aws sns delete-topic \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic"
```