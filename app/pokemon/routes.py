from flask_restful import Api
from flask import current_app as app

from .resources import PokemonApi

api = Api(app)

api.add_resource(
    PokemonApi,
    "/pokemon",
    endpoint="pokemon"
)