from .models import Users

class UserManager:
    
    @staticmethod
    def get(filters):
        """
        Retrieves list of pokemon objects
        :param filters, dict
        :return: List of pokemons objects
        """
        user = Users.query.filter_by(**filters).first()
        return user