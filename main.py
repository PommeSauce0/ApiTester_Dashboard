from flask import Flask, render_template, request, url_for, flash
from forms import SessionForm
from mongodb import MongoCon


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
    if form.validate_on_submit():
        results = MongoCon().get_results({'session_id': form.session_id.data})
        flash(f'Loaded {len(results)} documents.', 'success')
    else:
        results = MongoCon().get_results({})
    return render_template('session.html', title='Results', form=form, results=results)


if __name__ == '__main__':
    app.run(debug=True)
