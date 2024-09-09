# Create SQS
In this example we are going to create Standard, FIFO SQS Queue using CloudFormation

## Init
```sh
cd sqs/create-queue/cloudformation
chmod +x standard/deploy
chmod +x fifo/deploy
```

## Create Standard SQS Queue 
Execute deploy to create Standard SQS Queue `StandardQueue`
```sh
./standard/deploy
```

## Create FIFO SQS Queue 
Execute deploy to create FIFO SQS Queue `FifoQueue.fifo`
```sh
./fifo/deploy
```

## Cleanup
#### Delete Cloudformation stack for Standard Queue
```sh
aws cloudformation delete-stack \
--stack-name my-standard-sqs-stack
```

#### Delete Cloudformation stack for FIFO Queue
```sh
aws cloudformation delete-stack \
--stack-name my-fifo-sqs-stack
```