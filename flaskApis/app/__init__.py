from flask import Flask
from app.routes.pokemon_route import pokemon_blp

app = Flask(__name__)


app.register_blueprint(pokemon_blp, url_prefix="/pokemons")
