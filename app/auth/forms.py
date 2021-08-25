from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
  email = StringField('Email Address', validators=[Required(), Email()])
  password = PasswordField('Password', validators=[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Sign In')

class Registration(FlaskForm):
  email = StringField('Email Address', validators=[Required(), Email()])
  username = StringField('Username', validators=[Required()])
  fname = StringField('First Name', validators=[Required()])
  sname = StringField('Second Name', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('pass_confirm', message = 'Passwords Must Match')])
  pass_confirm = PasswordField('Confirm Password', validators = [Required()])
  submit = SubmitField()
