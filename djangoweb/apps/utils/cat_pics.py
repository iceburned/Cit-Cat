import asyncio
import json
from urllib.request import Request, urlopen


def get_response(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req_data = Request(url, headers=hdr)
    if req_data:
        data = urlopen(req_data).read()
        return data
    else:
        print("Error receiving data")
        return None


def main_cat():
    url_data = "https://api.thecatapi.com/v1/images/search"
    try:
        joke = get_response(url_data)
        json_data = json.loads(joke)
        return json_data[0]['url']
    except Exception:
        return "https://ms.storyasset.link/GvMLkxrjQUdFDJMWxRDyH1bEFzh1/11-affectionate-cat-breeds-ms-mqhvxzghjj.jpg"


if __name__ == '__main__':
    main_cat()


