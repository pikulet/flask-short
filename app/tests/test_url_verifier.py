import unittest
from app.url_verifier import UrlVerifier
from app.url_parser import UrlParser

class TestUrlVerifier(unittest.TestCase):

    def test_verify_invalid_format(self):
        self.assertFalse(
            UrlVerifier.is_url_valid(UrlParser.HTTP, "apples"))

    def test_verify_invalid_timeout(self):
        self.assertFalse(
            UrlVerifier.is_url_valid(UrlParser.HTTP,
                                     "www.randomnonexistentwebsite.com"))

    def test_verify_valid_http(self):
        self.assertTrue(
            UrlVerifier.is_url_valid(UrlParser.HTTP, "github.com"))

    def test_verify_valid_https(self):
        self.assertTrue(
            UrlVerifier.is_url_valid(UrlParser.HTTPS, "github.com"))

if __name__ == '__main__':
    unittest.main()


