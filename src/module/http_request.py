import asyncio
import aiohttp
from urllib.parse import urlparse


class HttpRequest:
    def __init__(
        self,
        url,
        method="GET",
        auth_token=None,
        poll_period=0,
        response_type="JSON",
        payload=None,
        header=None,
    ):
        self.url = url
        self.method = method
        self.auth_token = auth_token
        self.poll_period = poll_period
        self.response_type = response_type
        self.payload = payload
        self.header = header

        parsed_url = urlparse(self.url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError(f"Invalid URL: {self.url}")

    async def send_request(self):
        headers = {}
        if self.header:
            headers.update(self.header)

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
                if self.response_type == "JSON":
                    return await response.json()
                else:
                    return await response.text()

    async def poll(self):
        while True:
            response = await self.send_request()
            print(response)
            if self.poll_period == 0:
                break
            await asyncio.sleep(self.poll_period)
