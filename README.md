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

Public demo is currently INACTIVE. Feel free to host this on your own.

### :one: Enter URL to shorten

<img src="https://user-images.githubusercontent.com/24848927/105485513-f73b6e00-5ce7-11eb-96a9-6bf1ff28c89a.png" height="150">

### :two: Returns shortened result
<img src="https://user-images.githubusercontent.com/24848927/105485565-0e7a5b80-5ce8-11eb-9901-60f08c9a62db.png" height="100">

### :three: Delete a shortened entry
<img src="https://user-images.githubusercontent.com/24848927/105485608-1fc36800-5ce8-11eb-8b1b-ae58070509f8.png" height="100">

### :four: Only shorten valid entries
<img src="https://user-images.githubusercontent.com/24848927/105485637-2fdb4780-5ce8-11eb-8dba-72ff7c6c1b3f.png" height="150">

<img src="https://user-images.githubusercontent.com/24848927/105485656-38338280-5ce8-11eb-9a9d-d5c167452c69.png" height="100">

## :wrench: Run Tests

`python3 -m unittest discover -s app.tests -v`

## :seedling: Improvements

1. Check for hash collisions
2. Better method to validate URLs. Waiting for `requests` timeout can be quite long.
3. Caching entries
4. Nicer UI
5. Many more....



