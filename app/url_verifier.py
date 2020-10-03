import requests

class UrlVerifier:

    @staticmethod
    def is_url_valid(url):
        req = requests.get(url)
        return req.status_code == 200
