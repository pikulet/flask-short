class UrlParser:

    HTTP = "http://"
    HTTPS = "https://"

    @staticmethod
    def parse(url):
        if url.startswith(UrlParser.HTTP):
            return UrlParser.HTTP, url[len(HTTP): ]
        elif url.startswith(UrlParser.HTTPS):
            return UrlParser.HTTPS, url[len(HTTPS): ]
        else:
            return UrlParser.HTTP, url
