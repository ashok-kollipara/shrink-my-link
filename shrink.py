#!/usr/bin/env python

import asyncio
import aiohttp
import json
from src import constants as constants

class Shorten: 

    def __init__(self, long_url, custom_alias):
        self.long_url = long_url
        self.custom_alias = custom_alias

    async def tinyurl(self):

        url = constants.TINYURL_ROUTE

        headers = constants.HEADERS 
        headers['Authorization'] = f'Bearer {constants.TINYURL_TOKEN}'

        # recommened to use via json.dumps instead of plain dict type
        payload = json.dumps(
                {
                'url': self.long_url,
                'domain': 'tiny.one',
                'alias': self.custom_alias
                }
            )

        async with aiohttp.ClientSession(headers=headers) as session:

            async with session.post(url, data=payload) as reply:

                #print(f"TinyURL Status : {reply.status} - {reply.reason}")

                if reply.ok:
                    #convert the text from response received to python dict
                    txt = await reply.text()
                    result = json.loads(txt)
                    #print(f"type of result {type(result)}")
                    print(f"TinyUrl : {result['data']['tiny_url']}")

    async def cuttly(self):

        url = constants.CUTTLY_ROUTE+'?' + f'key={constants.CUTTLY_TOKEN}'
        url += '&'+ f'short={self.long_url}'
        url += '&'+ f'name={self.custom_alias}'

        headers = constants.HEADERS 

        async with aiohttp.ClientSession(headers=headers) as session:

            async with session.get(url) as reply:

                #print(f"Cuttly Status : {reply.status} - {reply.reason}")

                if reply.ok:
                    #convert the text from response received to python dict
                    txt = await reply.text()
                    result = json.loads(txt)
                    print(f"Cuttly : {result['url']['shortLink']}")

async def main():

    long_url = input('Enter your URL : ')
    custom_alias = input('Enter your alias for URL [5 - 20] chars long: ')

    print()

    test = Shorten(long_url, custom_alias)

    tasks = [ asyncio.create_task(test.cuttly()) ]
    
    tasks.append( asyncio.create_task(test.tinyurl()) )

    await asyncio.gather(*tasks)

    print()

if __name__ == '__main__':

    asyncio.run(main())
