#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
The body of the response must be displayed like this (tabulation before -)"""

import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
