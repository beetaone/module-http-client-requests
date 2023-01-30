"""
Entrypoint file that sets up and starts REST API server for the module.
"""

from os import getenv
from logging import getLogger
from bottle import run
from api import setup_logging
from module import module_main

setup_logging()
log = getLogger("main")


def main():
    log.info(
        "%s running with end-point set to %s",
        getenv("MODULE_NAME"),
        getenv("EGRESS_URLS"),
    )

    # start the server
    run(
        host="0.0.0.0",
        port=getenv("HOST_PORT"),
        quiet=True,
    )


if __name__ == "__main__":
    main()
