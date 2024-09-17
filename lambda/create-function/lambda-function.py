import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("This is a log message from Lambda!")
    return {
        'statusCode': 200,
        'body': 'Check CloudWatch Logs for the message!'
    }
