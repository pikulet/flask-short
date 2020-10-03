from app import db
from app.url_generator import SHA256Shortener
from app.models import UrlMapping

class UrlManager:

    def __init__(self, generator=SHA256Shortener()):
        self.generator = generator
        
    def get_short_url(self, long_url):
        # check if value exists in db 
        data = UrlMapping.query.filter_by(long_url=long_url).first()
        if data is not None:
            return data.serialise()['short_url']

        # shorten value
        short_url = self.generator.shorten(long_url)
        self.__save_data(long_url, short_url)
        return short_url

    def get_long_url(self, short_url):
        data = UrlMapping.query.filter_by(short_url=short_url).first()
        if data is not None:
            return data.serialise()['long_url']

        # data does not exist
        return None

    def __save_data(self, long_url, short_url):
        new_mapping = UrlMapping(long_url, short_url)
        db.session.add(new_mapping)
        db.session.commit()

url_manager = UrlManager()
