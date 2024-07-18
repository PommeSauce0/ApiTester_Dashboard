from flask import render_template, flash
from . import app
from .forms import SessionForm
from .mongodb import MongoCon
from .utils import build_query, percent_calc


@app.route('/', methods=['GET'])
def index():
    form = SessionForm()

    sessions = MongoCon().get_results({}, limit=50)
    sorted_sessions = dict()
    sorted_services = dict()

    for session in sessions:
        try:
            sorted_sessions[session['session_id']]['total'] += 1
        except KeyError:
            sorted_sessions[session['session_id']] = {'val': 0, 'total': 1}

        try:
            sorted_services[session['service']]['total'] += 1
        except KeyError:
            sorted_services[session['service']] = {'val': 0, 'total': 1}

        if session['status']:
            sorted_sessions[session['session_id']]['val'] += 1
            sorted_services[session['service']]['val'] += 1

    return render_template(
        template_name_or_list='index.html',
        form=form,
        sessions={key: percent_calc(**sorted_session) for key, sorted_session in sorted_sessions.items()},
        services={key: percent_calc(**sorted_service) for key, sorted_service in sorted_services.items()}
    )


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

    return render_template(
        template_name_or_list='session.html',
        title='Results',
        form=form,
        results=results,
        results_percents=percent_calc(len([result for result in results if result['status']]), len(results)),
        session_ids=session_ids
    )


@app.route('/session/<_id>', methods=['GET'])
def session_details(_id):
    return render_template(
        template_name_or_list='details.html',
        title='Details',
        session=MongoCon().get_document_by_id(_id)
    )
