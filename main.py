from flask import Flask, render_template, request, url_for, flash
from forms import SessionForm
from mongodb import MongoCon
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '63e34e3e00fed106c2aef6f6dcac624f'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/session', methods=['GET', 'POST'])
def session():
    form = SessionForm()
    session_ids = [id['session_id'] for id in MongoCon().get_results({}, select={'session_id': 1, '_id': 0})]

    if form.validate_on_submit():
        results = MongoCon().get_results({'session_id': form.session_id.data})
        flash(f'Loaded {len(results)} documents.', 'success')
    else:
        results = MongoCon().get_results({})

    results_percents = int(len([result for result in results if result['status']]) / len(results) * 100)
    return render_template('session.html', title='Results', form=form, results=results,
                           results_percents=results_percents, session_ids=session_ids)


@app.route('/session/<session_id>', methods=['GET'])
def session_details(session_id):
    return render_template('details.html', title='Details', session_id=session_id)


@app.template_filter('from_timestamp')
def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)


if __name__ == '__main__':
    app.run(debug=True)
