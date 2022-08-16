#!/usr/bin/env python

import requests
import json
import os

def cuttly():

    headers = { 
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
            'accept' : 'application/json',
            'Content-Type' : 'application/json'
            }

    long_url = input('Enter your URL : ')
    custom_alias = input('Enter your alias for URL [5 - 20] chars long: ')

    url = os.getenv('CUTTLY_ROUTE') + '?' + f"key={os.getenv('CUTTLY_TOKEN')}"
    url += '&'+ f'short={long_url}'
    url += '&'+ f'name={custom_alias}'

    #print(url)

    reply = requests.get(url, headers=headers)

    print(f"Status : {reply.status_code}")
    if reply.ok:
        #convert the text from response received to python dict
        result = json.loads(reply.text)
        print(f"Shrunk URL: {result['url']['shortLink']}")

if __name__ == '__main__':

    cuttly()
