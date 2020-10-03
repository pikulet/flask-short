import os

class DevelopmentConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'csrf key'

    POSTGRES_URL = os.environ.get("POSTGRES_URL")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PW = os.environ.get("POSTGRES_PW")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL

class DeployConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'csrf key'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
