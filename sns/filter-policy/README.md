# Create a topic
In this example we are going to create SNS topic and subscription with a filter policy.

## Create Standard `BookNotifications` SNS topic:
```sh
aws sns create-topic \
--name BookNotifications
```

## Create Subscription
Create a subscription with a filter policy to receive only messages with the book type **Thriller**.

Replace `topic-arn` with your topic's ARN and `your-email@example.com` with the email address you want to subscribe:
```sh
aws sns subscribe \
--topic-arn arn:aws:sns:us-west-2:123456789012:my-topic \
--protocol email \
--notification-endpoint your-email@example.com \
--attributes '{"FilterPolicy":"{\"type\": [\"Thriller\"]}"}'
```

## Confirm Subscription
* **Check Your Email**: You will receive an email from AWS SNS containing a confirmation link
* **Confirm Subscription**: Click the confirmation link in the email to complete the subscription process

## Test
Publish a message to your SNS topic.

Replace `topic-arn` with your topic's ARN:

#### Publish a Thriller Book Message
```sh
aws sns publish \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
--message "New thriller book released: The Mystery of the Night" \
--message-attributes '{"type":{"DataType":"String","StringValue":"Thriller"}}'
```

#### Publish a Romance Book Message
```sh
aws sns publish \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
--message "New romance book released: Love in the Air" \
--message-attributes '{"type":{"DataType":"String","StringValue":"Romance"}}'
```

Check your email to view the incoming requests and messages. You should receive only one message with a Thriller book

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

#### Delete topic
Replace `topic-arn` with your topic's ARN
```sh
aws sns delete-topic \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic"
```