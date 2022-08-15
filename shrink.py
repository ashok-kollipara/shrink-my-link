#!/usr/bin/env python

import argparse
import asyncio
import aiohttp
import json
from src import constants as constants

class Shorten: 

    def __init__(self, long_url, custom_alias, verbosity):
        self.long_url = long_url
        self.custom_alias = custom_alias
        self.verbosity = verbosity

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

                if self.verbosity:
                    print(f"TinyURL Status : {reply.status} - {reply.reason}")

                if reply.ok:
                    #convert the text from response received to python dict
                    txt = await reply.text()
                    result = json.loads(txt)
                    #print(f"type of result {type(result)}")
                    if self.verbosity:
                        print(f"TinyUrl : {result['data']['tiny_url']}")
                    else:
                        print(result['data']['tiny_url'])

    async def cuttly(self):

        url = constants.CUTTLY_ROUTE+'?' + f'key={constants.CUTTLY_TOKEN}'
        url += '&'+ f'short={self.long_url}'
        url += '&'+ f'name={self.custom_alias}'

        headers = constants.HEADERS 

        async with aiohttp.ClientSession(headers=headers) as session:

            async with session.get(url) as reply:

                if self.verbosity:
                    print(f"Cuttly Status : {reply.status} - {reply.reason}")

                if reply.ok:
                    #convert the text from response received to python dict
                    txt = await reply.text()
                    result = json.loads(txt)

                    if self.verbosity:
                        print(f"Cuttly : {result['url']['shortLink']}")
                    else:
                        print(result['url']['shortLink'])

async def main(long_url, custom_alias, verbosity, quickmode):

    '''
    print(long_url)
    print(custom_alias)
    print(verbosity)
    '''

    print()

    test = Shorten(long_url, custom_alias, verbosity)

    tasks = [ asyncio.create_task(test.cuttly()) ]
    
    if quickmode:
        tasks.append( asyncio.create_task(test.tinyurl()) )

    await asyncio.gather(*tasks)

    print()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="shrink", description="To shorten the given Long URL")

    # traditional arguments

    parser.add_argument("URL", type=str, help="the long url to shorten")
    parser.add_argument("-v", "--verbose", action="store_true", help="add verbosity to output")

    # below two arguments can be changed to mutually exclusive group
    # user can modify as per usage scope viz; parser.add_mutually_exclusive_group()

    parser.add_argument("-a", "--alias", action="store", default="", help="try for custom back-half e.g bit.ly/{ALIAS}")
    parser.add_argument("-q", "--quick", action="store_false", help="quickly get single link, useful to chain commands in Linux")

    args = parser.parse_args()

    if args.verbose:

        print (f"URL to be shortened : {args.URL}")

        if args.alias:
            print(f"alias chosen is : {args.alias}")

    asyncio.run(main(args.URL, args.alias, args.verbose, args.quick))
