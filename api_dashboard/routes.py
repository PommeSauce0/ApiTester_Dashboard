from flask import render_template, flash
from . import app
from .forms import SessionForm
from .mongodb import MongoCon
from .utils import build_query, percent_calc

@app.route('/', methods=['GET'])
def index():
    form = SessionForm()
    db = MongoCon()
    session_ids = [id['session_id'] for id in db.get_results(select={'session_id': 1, '_id': 0})]

    results = db.get_results(build_query(form)) if form.validate_on_submit() else db.get_results({})

    sessions = {}
    service_success_counts = {}

    for result in results:
        session_id = result['session_id']
        if session_id not in sessions:
            sessions[session_id] = []
        sessions[session_id].append(result)

        service = result.get('service', 'unknown')
        if service not in service_success_counts:
            service_success_counts[service] = {'success': 0, 'total': 0}

        service_success_counts[service]['total'] += 1
        if result['status']:
            service_success_counts[service]['success'] += 1

    unique_results = [session_results[0] for session_results in sessions.values()][:10]
    for session_data in unique_results:
        session_data['has_errors'] = any(not result['status'] for result in sessions[session_data['session_id']])

    service_success_rates = {service: percent_calc(data['success'], data['total']) for service, data in service_success_counts.items()}

    return render_template(
        'index.html',
        title='Index',
        form=form,
        results=unique_results,
        results_percents=percent_calc(len([result for result in unique_results if result['status']]), len(unique_results)),
        session_ids=session_ids,
        service_success_rates=service_success_rates
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
