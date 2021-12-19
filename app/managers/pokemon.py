from models.pokemon import Pokemon

class PokemonManager:
    
    @staticmethod
    def read(filters, order_by_param):
        """
        Retrieves list of pokemon objects
        :param filters, dict
        :return: List of pokemons objects
        """
        pokemons = Pokemon.query.filter(*filters).order_by(*order_by_param).all()
        return pokemons