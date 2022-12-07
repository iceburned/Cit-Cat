import asyncio
import json
from urllib.request import Request, urlopen

import httpx


def get_response(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req_data = Request(url, headers=hdr)
    if req_data:
        data = urlopen(req_data).read()
        print('----------downloaded cat image ------------')
        return data
    else:
        print("Error receiving data")
        return None

# async def get_response(url):
#     async with httpx.AsyncClient() as client:
#         r = await client.get(url)
#
#     return r


def main_cat():
    url_data = "https://api.thecatapi.com/v1/images/search"
    joke = get_response(url_data)

    json_data = json.loads(joke)
    # print(joke[0]['url'])
    return json_data[0]['url']


if __name__ == '__main__':
    main_cat()


