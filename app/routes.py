from flask import render_template, redirect, url_for, request
from app import app, db, SHORTENED_LENGTH, WEBSITE
from app.forms import EnterShortURLForm, ReturnToMainButton
from app.url_manager import url_manager
from app.url_verifier import UrlVerifier
from app.url_parser import UrlParser

APP_TITLE = "URL Service by Joyce"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EnterShortURLForm()

    if form.validate_on_submit():
        return redirect(url_for('short', url=form.url.data))

    return render_template('index.html', title=APP_TITLE, 
                           form=form)

@app.route('/short', methods=['GET', 'POST'])
def short():
    back_btn = ReturnToMainButton()
    if back_btn.validate_on_submit():
        return redirect('/')

    long_url = request.args['url']
    protocol, long_url = UrlParser.parse(long_url)
    is_url_valid = UrlVerifier.is_url_valid(protocol, long_url)
    if not is_url_valid:
        return redirect_invalid("I will only shorten valid URLs")

    short_url = url_manager.get_short_url(long_url)
    short_url = WEBSITE + short_url
    return render_template('result.html', title=APP_TITLE, 
                           short_url=short_url, back_btn=back_btn)

@app.route('/<short_url>', methods=['GET', 'POST'])
def long(short_url):
    back_btn = ReturnToMainButton()
    if back_btn.validate_on_submit():
        return redirect('/')

    if len(short_url) != SHORTENED_LENGTH:
        return redirect_invalid("Oh no! The short URL is invalid.")

    long_url = url_manager.get_long_url(short_url)

    if long_url is None:
        return redirect_invalid("Oh no! The short URL is invalid.")

    return redirect('http://' + long_url, code=302)


def redirect_invalid(message):
    back_btn = ReturnToMainButton()
    if back_btn.validate_on_submit():
        return redirect('/')

    return render_template('invalid.html', title=APP_TITLE,
                           message=message, back_btn=back_btn)
