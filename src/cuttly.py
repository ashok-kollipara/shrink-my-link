#!/usr/bin/env python

import constants
import requests
import json

def cuttly():

    headers = constants.HEADERS 

    long_url = input('Enter your URL : ')
    custom_alias = input('Enter your alias for URL [5 - 20] chars long: ')

    url = constants.CUTTLY_ROUTE+'?' + f'key={constants.CUTTLY_TOKEN}'
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
