from flask import render_template, url_for, flash
from . import app
from .forms import SessionForm
from .mongodb import MongoCon



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/session', methods=['GET', 'POST'])
def session():
    form = SessionForm()
    session_ids = [id['session_id'] for id in MongoCon().get_results(select={'session_id': 1, '_id': 0})]

    if form.validate_on_submit():
        results = MongoCon().get_results({'session_id': form.session_id.data})
        flash(f'Loaded {len(results)} documents.', 'success')
    else:
        results = MongoCon().get_results({})

    return render_template(
        template_name_or_list='session.html',
        title='Results',
        form=form,
        results=results,
        results_percents=int(len([result for result in results if result['status']]) / len(results) * 100),
        session_ids=session_ids
    )


@app.route('/session/<_id>', methods=['GET'])
def session_details(_id):
    return render_template(
        template_name_or_list='details.html',
        title='Details',
        session=MongoCon().get_document_by_id(_id)
    )
