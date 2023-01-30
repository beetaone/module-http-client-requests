import asyncio
import aiohttp

class HttpRequest:
    def __init__(self, url, method='GET', auth_token=None, poll_period=0, response_type='JSON', payload=None, header=None):
        self.url = url
        self.method = method
        self.auth_token = auth_token
        self.poll_period = poll_period
        self.response_type = response_type
        self.payload = payload
        self.header = header

    async def send_request(self):
        headers = {}
        if self.header:
            headers.update(self.header)

        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"

        async with aiohttp.ClientSession() as session:
            if self.method == 'GET':
                async with session.get(self.url, headers=headers) as response:
                    if self.response_type == 'JSON':
                        return await response.json()
                    else:
                        return await response.text()
            elif self.method == 'POST':
                async with session.post(self.url, headers=headers, json=self.payload) as response:
                    if self.response_type == 'JSON':
                        return await response.json()
                    else:
                        return await response.text()
            elif self.method == 'PUT':
                async with session.put(self.url, headers=headers, json=self.payload) as response:
                    if self.response_type == 'JSON':
                        return await response.json()
                    else:
                        return await response.text()
            elif self.method == 'DELETE':
                async with session.delete(self.url, headers=headers) as response:
                    if self.response_type == 'JSON':
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
