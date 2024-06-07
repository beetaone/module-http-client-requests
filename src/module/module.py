"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
import asyncio
import requests


log = getLogger("module")


async def module_main(configuration):
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Starting module ...")

    try:
        while True:
            log.debug("Configuration: %s", configuration)
            response = requests.request(
                configuration["METHOD"],
                configuration["URL"],
                headers=configuration["HEADER"],
                data=configuration["PAYLOAD"],
            )
            status = response.status_code
            body = response.text
            # status, body = await request.r
            if int(status / 100) != 2:
                log.error(f"Got response with status {status}: {body}")
            else:
                log.debug(f"Response: {body}")
                send_error = send_data(body)

                if send_error:
                    log.error(send_error)
                else:
                    log.debug("Data sent sucessfully.")

            if configuration["POLL_INTERVAL"] <= 0:
                break

            await asyncio.sleep(configuration["POLL_INTERVAL"])

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
