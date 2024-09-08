# Create a subscription to the topic
In this example, we will create an SNS topic and a subscription to it, and then try to publish a message using the CLI.

## Create Standard SNS topic
```sh
aws sns create-topic \
--name MySNSTopicCLI
```

## Create Subscription
To test the subscription, we will use the HTTP/HTTPS protocol with `Webhook.site`, which provides a temporary URL to which you can send HTTP requests and inspect them.

Replace topic-arn with your topic's ARN and notification-endpoint with the URL provided by Webhook.site
```sh
aws sns subscribe \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
--protocol https \
--notification-endpoint https://<webhook.site-url>
```

## Test
Publish a message to your SNS topic:
```sh
aws sns publish \
--topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
--message "This is a test message"
```
Visit your Webhook.site dashboard to view the incoming requests and messages.

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