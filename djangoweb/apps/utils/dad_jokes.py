from urllib.request import Request, urlopen


def get_response(url):
    hdr = {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/plain'}
    req_data = Request(url, headers=hdr)
    if req_data:
        data = urlopen(req_data).read()
        return data
    else:
        print("Error receiving data")
        return None


def main():
    url_data = "https://icanhazdadjoke.com/"
    joke = get_response(url_data).decode('UTF-8')
    return joke


if __name__ == '__main__':
    main()
