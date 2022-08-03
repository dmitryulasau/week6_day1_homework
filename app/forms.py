from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from app import app
from wtforms.validators import DataRequired, Email

class FindPokemon(FlaskForm):
    name = StringField('ENTER POKEMON\'S NAME OR NUMBER', validators=[DataRequired()])
    submit = SubmitField('CATCH HIM!')
  
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')