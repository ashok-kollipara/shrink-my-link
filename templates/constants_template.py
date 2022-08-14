#!/usr/bin/env python

"""

1. Register on your favourite service 
2. Obtain your personal API TOKEN
3. Edit this with respective vales mentioned in 'UPPERCASE'
4. Move this file to in 'src' folder as 'constants.py'

"""

HEADERS = {
            'user-agent' : 'YOUR_DESIRED_USER_AGENT_HERE',
            'accept' : 'application/json',
            'Content-Type' : 'application/json'
            }

# Tiny URL details
TINYURL_ROUTE = 'RESPECTIVE_API_ENDPOINT_HERE'
TINYURL_TOKEN = 'YOUR_TOKEN_HERE'

# Bitly details
BITLY_ROUTE = 'RESPECTIVE_API_ENDPOINT_HERE'
BITLY_TOKEN = 'YOUR_TOKEN_HERE'

# Cuttly details
CUTTLY_ROUTE = 'RESPECTIVE_API_ENDPOINT_HERE'
CUTTLY_TOKEN = 'YOUR_TOKEN_HERE'
