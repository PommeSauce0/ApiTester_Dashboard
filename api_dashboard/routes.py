from flask import render_template, url_for, flash
from . import app
from .forms import SessionForm
from .mongodb import MongoCon
from .utils import build_query


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/help', methods=['GET'])
def help():
    return render_template('help.html', title='Help')


@app.route('/session', methods=['GET', 'POST'])
def session():
    form = SessionForm()
    session_ids = [id['session_id'] for id in MongoCon().get_results(select={'session_id': 1, '_id': 0})]

    if form.validate_on_submit():
        results = MongoCon().get_results(build_query(form))
        flash(f'Loaded {len(results)} documents.', 'success')
    else:
        results = MongoCon().get_results({})

    try:
        results_percents = int(len([result for result in results if result['status']]) / len(results) * 100)
    except ZeroDivisionError:
        results_percents = 100

    return render_template(
        template_name_or_list='session.html',
        title='Results',
        form=form,
        results=results,
        results_percents=results_percents,
        session_ids=session_ids
    )


@app.route('/session/<_id>', methods=['GET'])
def session_details(_id):
    return render_template(
        template_name_or_list='details.html',
        title='Details',
        session=MongoCon().get_document_by_id(_id)
    )
