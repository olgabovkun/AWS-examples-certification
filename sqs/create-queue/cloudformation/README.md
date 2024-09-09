# Create SQS
In this example we are going to create Standard, FIFO SQS Queue using CloudFormation

## Create Standard SQS Queue 
Moved to the right directory
```sh
cd sqs/create-queue-cloudformation/standard
chmod +x deploy
```

Execute deploy to create Standard SQS Queue `StandardQueue`
```sh
./deploy
```

## Create FIFO SQS Queue 
Moved to the right directory
```sh
cd sqs/create-queue-cloudformation/fifo
chmod +x deploy
```

Execute deploy to create FIFO SQS Queue `FifoQueue.fifo`
```sh
./deploy
```

## Cleanup
#### Delete Cloudformation stack for Standard Queue
```sh
aws cloudformation delete-stack \
--stack-name my-fifo-sqs-stack
```

#### Delete Cloudformation stack for FIFO Queue
```sh
aws cloudformation delete-stack \
--stack-name my-standard-sqs-stack
```