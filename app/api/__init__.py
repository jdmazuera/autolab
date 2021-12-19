from flask_restful import Api
from app import app
from app.api.resources.pokemon import PokemonApi

autolab_api = Api(app)

autolab_api.add_resource(
    PokemonApi,
    "/pokemon",
    endpoint="pokemon"
)

autolab_api.init_app(app)