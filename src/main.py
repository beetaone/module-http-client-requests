"""
Entrypoint file that sets up and starts REST API server for the module.
"""
import asyncio

from os import getenv
from logging import getLogger
from bottle import run
from api import setup_logging
from module import module_main


setup_logging()
log = getLogger("main")


async def main():
    log.info(
        "%s running with end-point set to %s",
        getenv("MODULE_NAME"),
        getenv("EGRESS_URLS"),
    )
    configuration = {
        "URL": getenv("URL"),
        "METHOD": getenv("METHOD"),
        "AUTH_TOKEN": getenv("AUTH_TOKEN"),
        "POLL_PERIOD": int(getenv("POLL_PERIOD")),
        "RESPONSE_TYPE": getenv("RESPONSE_TYPE"),
        "PAYLOAD": getenv("PAYLOAD"),
        "HEADER": getenv("HEADER"),
    }

    await module_main(configuration)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
