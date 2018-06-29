import logging
import os
import time

from rasa_core.channels.rest import HttpInputChannel
from rasa_core.remote import RemoteAgent
from channels import RasaChatInput

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")

    # instantiate the input channel you want to connect to
    input_channel = HttpInputChannel(
        5001, "/", RasaChatInput(os.environ.get("RASA_API_ENDPOINT_URL")))

    # makes sure core is available before we start the app
    time.sleep(60)

    agent = RemoteAgent.load('models/dialogue',
                             os.environ.get("RASA_REMOTE_CORE_ENDPOINT_URL"),
                             os.environ.get("RASA_CORE_TOKEN"))

    agent.handle_channel(input_channel)
