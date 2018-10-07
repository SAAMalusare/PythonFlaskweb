from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from OpsBuddy.db import logonstats


class UserOpsForm(FlaskForm):
    submit = SubmitField('Get last accessed nodes')

class GetNodesForm(FlaskForm):
    username = StringField('Username',render_kw={"placeholder": "Suhas"},validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Get Node list')

class GetRMSForm(FlaskForm):
    username = StringField('Username',render_kw={"placeholder": "Suhas"},validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Get List')

class GetUserMapForm(FlaskForm):
    username = StringField('Username',render_kw={"placeholder": "Suhas"},validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Get List')