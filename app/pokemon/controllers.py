from .managers import PokemonManager
from .models import Pokemon
from .serializers import PokemonSchema

class PokemonController:

    @staticmethod
    def retrieve_list(params, order_by_parameters):
        """
        Return list of pokemon json objects given a filters dict
        :param filters: dict, fitlers from request
        :return List of dicts
        """
        order_by_parameters = tuple(map(PokemonController.__map_order_by_param, order_by_parameters))
        params_fields = PokemonController.__string_to_fields_filters(params)
        pokemons = PokemonManager.read(params_fields, order_by_parameters)
        pokemon_serializer = PokemonSchema(many=True)
        pokemons_json = pokemon_serializer.dumps(pokemons)

        return pokemons_json

    @staticmethod
    def __map_order_by_param(param):
        field_name, order = param.split("__")
        field = getattr(Pokemon, field_name)
        return field.desc() if order == "desc" else field.asc()


    @staticmethod
    def __string_to_fields_filters(params):
        params_tuples = list(params.items())
        params_fields = []

        for filter, value in params_tuples:
            if type(value) == str:
                operation = getattr(Pokemon, filter).like("%{}%".format(value))
                params_fields.append(operation)
            elif "__" in filter:
                field_name, limit = filter.split("__")
                field = getattr(Pokemon, field_name)
                operation = getattr(Pokemon, field_name) >= value if limit == "gt" else getattr(Pokemon,field_name) <= value
                params_fields.append(operation)
            else:
                field = getattr(Pokemon, filter)
                operation = field == value
                params_fields.append(operation)
        
        return params_fields
