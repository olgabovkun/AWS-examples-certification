# Purge Queue
Deletes available messages in a queue (including in-flight messages) specified by the QueueURL parameter.

Update `queue-url`:
```sh
aws sqs purge-queue \
--queue-url https://sqs.<region>.amazonaws.com/<account-id>/<queue-name>
```