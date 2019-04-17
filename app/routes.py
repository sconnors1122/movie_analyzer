from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SubmissionForm
from app.analyzer import get_sentiment

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SubmissionForm()
    if form.validate_on_submit():
        sentiment = get_sentiment(form.review.data)
        flash('Review submitted for title {}, sentiment {}'.format(
            form.title.data, sentiment))
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)