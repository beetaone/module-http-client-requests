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
        payload=None,
        header=None,
    ):
        self.url = url
        self.method = method
        self.auth_token = auth_token
        self.payload = payload
        self.header = header

        log.debug(f"URL: {self.url}")
        log.debug(f"Method: {self.method}")

        parsed_url = urlparse(self.url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError(f"Invalid URL: {self.url}")

        self.headers = {}
        if self.header:
            self.headers.update(json.loads(self.header))

        if self.auth_token:
            self.headers["Authorization"] = f"Bearer {self.auth_token}"

    async def send_request(self):
        async with aiohttp.ClientSession() as session:
            request_map = {
                "GET": session.get,
                "POST": session.post,
                "PUT": session.put,
                "DELETE": session.delete,
            }

            method = request_map.get(self.method)
            if not method:
                raise ValueError(
                    f"Invalid method: {self.method}. Allowed methods are GET, POST, PUT, and DELETE"
                )
            async with method(
                self.url, headers=self.headers, json=self.payload
            ) as response:
                if response.headers["Content-Type"] == "application/json":
                    return response.status, await response.json()
                else:
                    return response.status, await response.text()
