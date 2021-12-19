from models.pokemon import Pokemon

class PokemonManager:
    
    @staticmethod
    def read(filters):
        """
        Retrieves list of pokemon objects
        :param filters, dict
        :return: List of pokemons objects
        """
        pokemons = Pokemon.query.filter_by(**filters).all()
        return pokemons