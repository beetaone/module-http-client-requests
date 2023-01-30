"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
import asyncio
from . import http_request

log = getLogger("module")


async def module_main(configuration):
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Starting module ...")

    try:
        # YOUR CODE HERE
        # ----------------------------------------------------------------
        request = http_request.HttpRequest(
            configuration["URL"],
            configuration["METHOD"],
            configuration["AUTH_TOKEN"],
            configuration["RESPONSE_TYPE"],
            configuration["PAYLOAD"],
            configuration["HEADER"],
        )

        while True:
            response = await request.send_request()
            log.debug(f"Response: {response}")
            send_error = send_data(response)

            if send_error:
                log.error(send_error)
            else:
                log.debug("Data sent sucessfully.")
            # print("response: ", response)
            # print("response type: ", type(response))

            await asyncio.sleep(configuration["POLL_PERIOD"])

        # ----------------------------------------------------------------

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
