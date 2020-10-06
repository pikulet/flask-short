import unittest
from app.url_parser import UrlParser

class TestUrlParser(unittest.TestCase):

    def test_parse_invalid(self):
        result = UrlParser.parse("apples")
        self.assertEqual(result, (UrlParser.HTTP, "apples"))

    def test_parse_valid_http_invalid_site(self):
        result = UrlParser.parse("http://www.randomnonexistentsite.com")
        self.assertEqual(result, (UrlParser.HTTP, "www.randomnonexistentsite.com"))

    def test_parse_valid_http(self):
        result = UrlParser.parse("http://www.google.com")
        self.assertEqual(result, (UrlParser.HTTP, "www.google.com"))

    def test_parse_valid_https(self):
        result = UrlParser.parse("https://www.google.com")
        self.assertEqual(result, (UrlParser.HTTPS, "www.google.com"))

    def test_parse_valid_no_protocol(self):
        result = UrlParser.parse("www.google.com")
        self.assertEqual(result, (UrlParser.HTTP, "www.google.com"))

if __name__ == '__main__':
    unittest.main()
