
from flask import render_template, request, url_for, flash, redirect
from app import app

from flask import render_template, flash, redirect
from .forms import FindPokemon, LoginForm
import requests


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Kevin or Dylan'}
    form = FindPokemon()

    if request.method =='POST':
        
        name = request.form.get('name')
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)

        if not response.ok:
            error_message = "We had an Unexpected Error"
            return render_template('index.html.j2', error=error_message)
        if not response.json():
            error_message = "We don't have this Pokemon's name"
            return render_template('index.html.j2', error=error_message)    
        data = response.json()
        
        pokemon_info = []
        
        pokemon_dict = {}
   
        pokemon_dict = {
            'name': data['name'],
            'ability': data['abilities'][0]['ability']['name'],
            'defense': data['stats'][2]['base_stat'],
            'attack': data['stats'][1]['base_stat'],
            'hp': data['stats'][0]['base_stat'],
            'image': data['sprites']['other']['official-artwork']['front_default'],
            'gif': data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
        }

        
        pokemon_info.append(pokemon_dict)

        return render_template('index.html.j2', info=pokemon_info, form=form, user=user)

    return render_template('index.html.j2', title='Home', user=user, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('login.html.j2', title='Sign In', form=form)