#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib
and displays the response body with type and content
"""

from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()  # cavabı bytes formatında alırıq

        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
