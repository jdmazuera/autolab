from flask_restful import Resource, reqparse
from flask import Response
from app.controllers.pokemon import PokemonController

class PokemonApi(Resource):
    def get(self):
        parameters = self.__get_parameters()
        print(parameters)
        response = PokemonController.retrieve_list(parameters)
        return Response(response,  mimetype='application/json')

    def __get_parameters(self):
        """
        Get request parameters
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, store_missing=False)
        parser.add_argument("type_1", type=str, store_missing=False)
        parser.add_argument("type_2", type=str, store_missing=False)
        parser.add_argument("total_stats", type=int, store_missing=False)
        parser.add_argument("health_points", type=int, store_missing=False)
        parser.add_argument("attack", type=int, store_missing=False)
        parser.add_argument("defense", type=int, store_missing=False)
        parser.add_argument("special_attack", type=int, store_missing=False)
        parser.add_argument("special_defense", type=int, store_missing=False)
        parser.add_argument("speed", type=int, store_missing=False)
        parser.add_argument("generation", type=int, store_missing=False)
        parser.add_argument("legendary", type=int, store_missing=False)

        return parser.parse_args()