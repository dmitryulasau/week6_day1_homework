from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

# class FindPokemon(FlaskForm):
#     pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])

class FindPokemon(FlaskForm):
    name = StringField('ENTER POKEMON\'S NAME', validators=[DataRequired()])
    submit = SubmitField('CATCH HIM!')
  

