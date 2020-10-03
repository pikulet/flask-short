from flask import render_template, redirect, url_for, request
from app import app, db, SHORTENED_LENGTH, WEBSITE
from app.forms import EnterShortURLForm
from app.url_manager import url_manager

APP_TITLE = "URL Service by Joyce"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EnterShortURLForm()

    if form.validate_on_submit():
        return redirect(url_for('short', url=form.url.data))

    return render_template('index.html', title=APP_TITLE, 
                           form=form)

@app.route('/short')
def short():
    original_url = request.args['url']
    short_url = url_manager.get_short_url(original_url)
    short_url = WEBSITE + short_url
    return render_template('result.html', 
                          title=APP_TITLE, short_url=short_url)
@app.route('/<short_url>')
def long(short_url):
    if len(short_url) != SHORTENED_LENGTH:
        return render_template('invalid.html', title=APP_TITLE)

    long_url = url_manager.get_long_url(short_url)

    if long_url is None:
        return render_template('invalid.html', title=APP_TITLE)

    return redirect('http://' + long_url, code=302)

