from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    review = PasswordField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')