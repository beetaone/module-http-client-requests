from logging import getLogger
from urllib.parse import urlparse
import json
import aiohttp


log = getLogger("module")


class HttpRequest:
    def __init__(
        self,
        url,
        method="GET",
        auth_token=None,
        response_type="JSON",
        payload=None,
        header=None,
    ):
        self.url = url
        self.method = method
        self.auth_token = auth_token
        self.response_type = response_type
        self.payload = payload
        self.header = header

        log.debug(f"URL: {self.url}")
        log.debug(f"Method: {self.method}")
        log.debug(f"Auth Token: {self.auth_token}")
        log.debug(f"Response Type: {self.response_type}")
        log.debug(f"Payload: {self.payload}")
        log.debug(f"Header: {self.header}")

        parsed_url = urlparse(self.url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError(f"Invalid URL: {self.url}")

    async def send_request(self):
        headers = {}
        if self.header:
            headers.update(json.loads(self.header))

        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"

        async with aiohttp.ClientSession() as session:
            method_map = {
                "GET": session.get,
                "POST": session.post,
                "PUT": session.put,
                "DELETE": session.delete,
            }

            method = method_map.get(self.method)
            if not method:
                raise ValueError(
                    f"Invalid method: {self.method}. Allowed methods are GET, POST, PUT, and DELETE"
                )

            async with method(self.url, headers=headers, json=self.payload) as response:
                # log.debug(f"Response status: {response.status}")
                # log.debug(f"Response headers: {response.headers}")
                # log.debug(f"Response content: {await response.text()}")

                return await response.text()

