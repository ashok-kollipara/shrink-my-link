#!/usr/bin/env python

import requests
import json
import os

def tinyurl():

    headers = {
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
            'accept' : 'application/json',
            'Content-Type' : 'application/json'
            }

    headers['Authorization'] = f"Bearer {os.getenv('TINYURL_TOKEN')}"

    url = os.getenv('TINYURL_ROUTE')

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
