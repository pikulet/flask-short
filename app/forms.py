from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EnterShortURLForm(FlaskForm):
    url = StringField('Enter URL to shorten here', validators=[DataRequired()])
    desired_short_url = StringField('Short URL here')
    submit = SubmitField('Help me shorten')

class ReturnToMainButton(FlaskForm):
    submit = SubmitField('Go back to main')
