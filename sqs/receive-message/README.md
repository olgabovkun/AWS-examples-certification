# Receive message from the specified queue

Retrieves one or more messages (up to 10), from the specified queue. 

Update `queue-url`:
```sh
aws sqs receive-message \
--queue-url https://sqs.<region>.amazonaws.com/<account-id>/<queue-name> \
--attribute-names All \
--message-attribute-names All \
--max-number-of-messages 10
```