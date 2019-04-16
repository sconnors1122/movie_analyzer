from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')