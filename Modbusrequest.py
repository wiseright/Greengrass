import sys
import datetime
import time
import logging
import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    PublishToTopicRequest,
    PublishMessage,
    BinaryMessage
)

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
FUTURE_WAIT_TIME = 10

SLEEP_TIME = 5

ipc_client = awsiot.greengrasscoreipc.connect()
topic = "modbus/request/conveyer"

message = '{ "id": "TestRequest_0_7", "function": "ReadCoils", "address": 00001, "quantity": 10 }'

logger.debug("topic: " + topic)
logger.debug("message: " + message)

request = PublishToTopicRequest()
request.topic = topic
publish_message = PublishMessage()
publish_message.binary_message = BinaryMessage()
publish_message.binary_message.message = bytes(message, "utf-8")
request.publish_message = publish_message

while True:
    operation = ipc_client.new_publish_to_topic()
    operation.activate(request)
    future = operation.get_response()
    future.result(FUTURE_WAIT_TIME)
    # Append the message to the log file.
    logger.info(message)
    print("VAI A DORMIRE ver 7")
    time.sleep(SLEEP_TIME)