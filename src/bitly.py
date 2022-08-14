#!/usr/bin/env python

import constants
import requests
import json

def bitly():

    headers = constants.HEADERS 
    headers['Authorization'] = f'Bearer {constants.BITLY_TOKEN}'

    url = constants.BITLY_ROUTE
    key = constants.BITLY_TOKEN

    long_url = input('Enter your URL : ')
    custom_alias = input('Enter your alias for URL [5 - 20] chars long: ')

    # recommened to use via json.dumps instead of plain dict type
    payload = json.dumps(
            {
            'long_url': long_url,
            'domain': 'bit.ly',
            }
        )

    reply = requests.post(url, headers=headers, data=payload)

    print(f"Status : {reply.status_code}")

    if reply.ok:
        #convert the text from response received to python dict
        result = json.loads(reply.text)
        print(f"Shrunk URL: {result['link']}")

if __name__ == '__main__':

    bitly()
