# flask-url-short
simple url shortener that actually makes urls longer 😂

### Setup

Install necessary dependencies...

`pip3 install virtualenv`

and

`source /venv/bin/activate`

### Local Development

In `app/__init__.py, set `app.config.from_object(DevelopmentConfig)

Modify `DevelopmentConfig` in `config.py` as necessary.

(Default) Setup postgresql, set environment variables:
`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PW`, `POSTGRES_URL`

`export FLASK_APP=app.py`
`flask run`

### Deploy

In `app/__init__.py, set `app.config.from_object(DeployConfig)

Modify `DeployConfig` in `config.py` as necessary.

(Default) Heroku-postgresql will have the environment variable `DATABASE_URL`.

### Improvements

1. Check for hash collisions
2. Better method to validate URLs. Waiting for `requests` timeout can be quite long.
3. Caching entries
4. Nicer UI
5. Many more....



