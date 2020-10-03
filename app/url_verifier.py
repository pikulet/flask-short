import requests

class UrlVerifier:

    @staticmethod
    def is_url_valid(protocol, url):
        req = requests.get(protocol + url)
        return req.status_code == 200
