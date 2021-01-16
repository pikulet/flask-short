# :test_tube: flask-short :test_tube:
A url shortener that actually makes urls longer 😂 (because of the heroku domain used)

## :dolphin: Setup

Install necessary dependencies...

`sudo apt install python3-flask`

Setup venv with 

`python3 -m pip install virtualenv`

and

`source /venv/bin/activate`

then install the python packages

`python3 -m pip install --user -r requirements.txt`

## :firecracker: Local Development

In `app/__init__.py, set `app.config.from_object(DevelopmentConfig)

Modify `DevelopmentConfig` in `config.py` as necessary.

(Default) Setup postgresql, set environment variables:
`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PW`, `POSTGRES_URL`

`export FLASK_APP=app.py`
`flask run`

## :zap: PostgreSQL on local environment

`sudo apt-get install -y postgresql`

This is the same as your operating system ID, which is required if you want to access the database using the same user.

`sudo -u postgres createdb joyce` 

This is the actual database for the application.

`sudo -u postgres createdb short`

Enter the database server using your own credentials, and specify the database. Refer to database.psql for the database scheme. Create the table as needed.

`psql -U joyce -d short`

Set the password as needed.

`ALTER USER joyce WITH PASSWORD 'joyce';`

For reference, I've added a sample `.env` file. Modify the fields as needed.

## :rocket: Deployment

In `app/__init__.py, set `app.config.from_object(DeployConfig)

Modify `DeployConfig` in `config.py` as necessary.

(Default) Heroku-postgresql will have the environment variable `DATABASE_URL`.

Install heroku-CLI.

`sudo snap install heroku --classic`

Login to heroku.

`heroku login`

Add heroku remote.

`git remote add heroku https://git.heroku.com/pikulet-short-url.git`

To deploy,

`git push heroku master`

## :cactus: Public Demo

As I'm running a public demo, I'm also displaying all my db mappings. To remove
errant entries, use `heroku pg:psql` to manage the db.

## :wrench: Run Tests

`python3 -m unittest discover -s app.tests -v`

## :seedling: Improvements

1. Check for hash collisions
2. Better method to validate URLs. Waiting for `requests` timeout can be quite long.
3. Caching entries
4. Nicer UI
5. Many more....



