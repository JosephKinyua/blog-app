from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
  email = StringField('Email Address', validators=[Required(), Email()])
  password = PasswordField('Password', validators=[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Sign In')
