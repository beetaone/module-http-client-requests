"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
from bottle import post, request, response

log = getLogger("module")


@post("/")
def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")

    try:
        # YOUR CODE HERE
        # ----------------------------------------------------------------

        # receive data from the previous module
        input_data = request.json

        log.debug("Received data: %s", input_data)

        # ----------------------------------------------------------------

        # send data to the next module
        send_error = send_data(input_data)

        if send_error:
            log.error(send_error)
            response.status = 400
            return f"Error: {send_error}"
        else:
            log.debug("Data sent successfully.")
            return "OK - data accepted"

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
        response.status = 400
        return f"Exception occurred in the successive module while handling your POST request. {e}"
