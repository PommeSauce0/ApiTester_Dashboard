from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class SessionForm(FlaskForm):
    session_id = StringField('Session ID', validators=[Length(max=22, message="Invalide Session ID")])
    service = StringField('Service')
    status = SelectField('Status', choices=[('01', ''), ('1', 'True'), ('', 'False')], default=('01', ''))
    env = SelectField('Environment',
                      choices=[('', ''), ('production', 'production'), ('recette', 'recette'), ('snapshot', 'snapshot'), ('localhost', 'localhost')],
                      default=('', ''))

    query = StringField('MongoDB query', validators=[])

    submit = SubmitField('Search')
