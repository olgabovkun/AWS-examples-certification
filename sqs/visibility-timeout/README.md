# Visibility Timeout Example
In this example we check that we cannot receive an SQS message during the visibility timeout. If the message is still being processed (i.e., within the visibility timeout), it should not be available for retrieval by any other consumer.

## Init
```sh
cd sqs/visibility-timeout/
chmod +x visibility-timeout
```

## Test
```sh
./visibility-timeout
```