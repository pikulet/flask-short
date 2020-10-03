from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EnterShortURLForm(FlaskForm):
    url = StringField('Enter URL to shorten here', validators=[DataRequired()])
    submit = SubmitField('Help me shorten')

