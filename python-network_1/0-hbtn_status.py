#!/usr/bin/python3
""" What's my status? tapmaliyiq """

from urllib import request
url="https://intranet.hbtn.io/status"
response=request.urlopen(url)
print(response.read())
