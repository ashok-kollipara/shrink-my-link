#!/usr/bin/env python

import constants
import requests
import json

def tinyurl():

    headers = constants.HEADERS 
    headers['Authorization'] = f'Bearer {constants.TINYURL_TOKEN}'

    url = constants.TINYURL_ROUTE
    key = constants.TINYURL_TOKEN

    long_url = input('Enter your URL : ')
    custom_alias = input('Enter your alias for URL [5 - 20] chars long: ')

    # recommened to use via json.dumps instead of plain dict type
    payload = json.dumps(
            {
            'url': long_url,
            'domain': 'tiny.one',
            'alias': custom_alias
            }
        )

    reply = requests.post(url, headers=headers, data=payload)

    print(f"Status : {reply.status_code}")

    if reply.ok:
        #convert the text from response received to python dict
        result = json.loads(reply.text)
        print(f"Shrunk URL: {result['data']['tiny_url']}")

if __name__ == '__main__':

    tinyurl()
