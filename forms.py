from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class SessionForm(FlaskForm):
    session_id = StringField('Session ID', validators=[DataRequired(), Length(min=22, max=22, message="Invalide Session ID")])

    status = SelectField('Status', choices=[(None, ''), (True, 'True'), (False, 'False')], default=(None, ''))

    query = StringField('MongoDB query', validators=[])

    submit = SubmitField('Search')
