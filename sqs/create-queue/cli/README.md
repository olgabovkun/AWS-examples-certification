# Create SQS
In this example we are going to create Standard, FIFO SQS Queue using AWS CLI

## Create Standard SQS Queue 
```sh
aws sqs create-queue \
--queue-name StandardQueue
```

## Create FIFO SQS Queue 
To create a FIFO (First-In-First-Out) SQS queue:
* The queue name must end with `.fifo` to indicate that it's a FIFO queue 
* You need to set the --attributes parameter:
  * FifoQueue=true - specifies that the queue is a FIFO queue
  * ContentBasedDeduplication=true - (Optional) enables content-based deduplication, meaning that messages with the same content will be treated as duplicates
```sh
aws sqs create-queue \
--queue-name FifoQueue.fifo \
--attributes FifoQueue=true,ContentBasedDeduplication=true
```

## Cleanup
#### Delete Standard Queue
Get Queue URL:
```sh
aws sqs get-queue-url \
--queue-name StandardQueue
```

Copy the queue URL from the previous step and insert it into the following `--queue-url` parameter.

Update `queue-url`, then delete the Queue:
```sh
aws sqs delete-queue \
--queue-url https://sqs.region.amazonaws.com/account-id/StandardQueue
```

#### Delete FIFO Queue
Get Queue URL:
```sh
aws sqs get-queue-url \
--queue-name FifoQueue.fifo
```

Copy the queue URL from the previous step and insert it into the following `--queue-url` parameter.

Update `queue-url`, then delete the Queue:
```sh
aws sqs delete-queue \
--queue-url https://sqs.region.amazonaws.com/account-id/FifoQueue.fifo
```
