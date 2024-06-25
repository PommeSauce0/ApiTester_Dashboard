from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SessionForm(FlaskForm):
    session_id = StringField('Session ID', validators=[DataRequired(), Length(min=22, max=22, message="Invalide Session ID")])

    submit = SubmitField('Search')
