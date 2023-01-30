"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
from http_request import HttpRequest

log = getLogger("module")


def module_main(configuration):
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")

    try:
        # YOUR CODE HERE
        # ----------------------------------------------------------------

        request = HttpRequest(
            configuration["URL"], configuration["METHOD"], configuration["AUTH_TOKEN"], configuration["POLL_PERIOD"],
            configuration["RESPONSE_TYPE"], configuration["PAYLOAD"], configuration["HEADER"]
        )

        # ----------------------------------------------------------------

        # send data to the next module
        send_error = send_data(request)

        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent sucessfully.")

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
