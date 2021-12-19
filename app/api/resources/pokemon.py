from flask_restful import Resource, reqparse
from flask import Response
from app.decorators.token_required import token_required
from app.controllers.pokemon import PokemonController


class PokemonApi(Resource):
    method_decorators = [token_required]

    def get(self):
        parameters = self.__get_parameters()
        parameters, order_by_parameters = self.__process_params(parameters)
        response = PokemonController.retrieve_list(
            parameters, order_by_parameters)
        return Response(response,  mimetype='application/json')

    def __get_parameters(self):
        """
        Get request parameters
        :param parameters: dict, values from request
        :return Dict
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
        parser.add_argument("order_by", type=str, store_missing=False)

        parser.add_argument("total_stats__lt", type=int, store_missing=False)
        parser.add_argument("total_stats__gt", type=int, store_missing=False)
        parser.add_argument("health_points__lt", type=int, store_missing=False)
        parser.add_argument("health_points__gt", type=int, store_missing=False)
        parser.add_argument("attack__lt", type=int, store_missing=False)
        parser.add_argument("attack__gt", type=int, store_missing=False)
        parser.add_argument("defense__lt", type=int, store_missing=False)
        parser.add_argument("defense__gt", type=int, store_missing=False)
        parser.add_argument("special_attack__lt",
                            type=int, store_missing=False)
        parser.add_argument("special_attack__gt",
                            type=int, store_missing=False)
        parser.add_argument("special_defense__lt",
                            type=int, store_missing=False)
        parser.add_argument("special_defense__gt",
                            type=int, store_missing=False)
        parser.add_argument("speed__lt", type=int, store_missing=False)
        parser.add_argument("speed__gt", type=int, store_missing=False)
        parser.add_argument("generation__lt", type=int, store_missing=False)
        parser.add_argument("generation__gt", type=int, store_missing=False)

        return parser.parse_args()

    def __process_params(self, parameters):
        """
        Process parameters from request
        :param parameters: dict, values from request
        :return Dict, List
        """
        order_by_parameters = []

        if parameters.get("order_by"):
            order_by_parameters = parameters["order_by"].split(",")
            del parameters["order_by"]

        return parameters, order_by_parameters
