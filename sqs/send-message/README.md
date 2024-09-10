# Send message to the specified queue

## Create Queue
If you dont have a queue
```sh
aws sqs create-queue \
--queue-name OrderNotificationQueue
```

## Send message
Update `queue-url`:
```sh
aws sqs send-message \
--queue-url https://sqs.<region>.amazonaws.com/<account-id>/<queue-name> \
--message-body "New order received: Order ID 56789 for Customer ID 98765" \
--delay-seconds 0 \
--message-attributes '{
    "CustomerID": {
        "StringValue": "98765",
        "DataType": "String"
    },
    "OrderID": {
        "StringValue": "56789",
        "DataType": "String"
    },
    "OrderPriority": {
        "StringValue": "High",
        "DataType": "String"
    }
}'
```