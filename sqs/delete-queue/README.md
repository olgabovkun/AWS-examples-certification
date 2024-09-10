# Delete Queue
Deletes the queue specified by the QueueUrl, regardless of the queue’s contents.

Update `queue-url`:
```sh
aws sqs delete-queue \
--queue-url https://sqs.<region>.amazonaws.com/<account-id>/<queue-name>
```