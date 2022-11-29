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
    joke = get_response(url_data)
    json_data = json.loads(joke)
    print(json_data[0]['url'])
    return json_data[0]['url']


if __name__ == '__main__':
    main_cat()
