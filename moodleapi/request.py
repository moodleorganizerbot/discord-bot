"""
Requests module responsable to get data from Moodle Platform.
"""

import aiohttp
import asyncio
import json

from moodleapi.settings import REQUEST


class Request:
    """Class Request is used for all type of request in API. Be very
    careful with the parameters."""

    def __init__(self, token):
        self.url = REQUEST + token

    def __str__(self):
        return f"Request object for {self.url}"

    def get(self, *args, **kwargs):
        """GET method receive the function according to func dict in settings.
        All params need to be passed with respectively values well-informed in API"""

        for key, value in kwargs.items():
            self.url += f"&{key}={value}"

        for elem in args:
            for key, value in elem.items():
                self.url += f"&{key}={value}"

        async def get(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.content.read()

        loop = asyncio.get_event_loop()

        try:
            r = json.loads(loop.run_until_complete(get(self.url)))

        except Exception as err:
            return f"HTTP error occurred: {err}. Check the parameters."

        else:
            return r

    def post(self, *args, **kwargs):
        pass
