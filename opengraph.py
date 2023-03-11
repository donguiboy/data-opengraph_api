# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""
import requests

def fetch_metadata(url):
    response = requests.get(f'https://opengraph.lewagon.com/?url={url}')
    if response.status_code == 200:
        return response.json()["data"]
    return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))
