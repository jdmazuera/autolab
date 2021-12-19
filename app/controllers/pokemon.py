from app.managers.pokemon import PokemonManager
from models.serializers.pokemon import PokemonSchema

class PokemonController:

    @staticmethod
    def retrieve_list(filters):
        """
        Return list of pokemon json objects given a filters dict
        :param filters: dict, fitlers from request
        :return List of dicts
        """
        pokemons = PokemonManager.read(filters)
        pokemon_serializer = PokemonSchema(many=True)
        pokemons_json = pokemon_serializer.dumps(pokemons)

        return pokemons_json