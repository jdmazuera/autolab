from itertools import pairwise
from base_context import BaseTest
from app.pokemon.serializers import PokemonSchema, Pokemon
from app import db


class TestPokemonAPI(BaseTest):

    def get_patches(self):
        return (
            'app.auth.decorators.token_required'
        )

    def create_data(self):
        pokemon_schema = PokemonSchema(many=True)
        pokemon_data = pokemon_schema.loads("""[
                    {
                        "attack": 10,
                        "type_1": "Water",
                        "type_2": null,
                        "name": "Magikarp",
                        "total_stats": 200,
                        "legendary": false,
                        "health_points": 20,
                        "special_defense": 20,
                        "defense": 55,
                        "speed": 80,
                        "special_attack": 15,
                        "generation": 1
                    },
                    {
                        "attack": 30,
                        "type_1": "Bug",
                        "type_2": null,
                        "name": "Caterpie",
                        "total_stats": 195,
                        "legendary": false,
                        "health_points": 45,
                        "special_defense": 20,
                        "defense": 35,
                        "speed": 45,
                        "special_attack": 20,
                        "generation": 1
                    },
                    {
                        "attack": 35,
                        "type_1": "Bug",
                        "type_2": "Poison",
                        "name": "Weedle",
                        "total_stats": 195,
                        "legendary": false,
                        "health_points": 40,
                        "special_defense": 20,
                        "defense": 30,
                        "speed": 50,
                        "special_attack": 20,
                        "generation": 1
                    },
                    {
                        "attack": 30,
                        "type_1": "Grass",
                        "type_2": null,
                        "name": "Sunkern",
                        "total_stats": 180,
                        "legendary": false,
                        "health_points": 30,
                        "special_defense": 30,
                        "defense": 30,
                        "speed": 30,
                        "special_attack": 30,
                        "generation": 2
                    }
                ]"""
                                            )
        with self.app.app_context():
            for row in pokemon_data:
                pokemon = Pokemon(**row)
                db.session.add(pokemon)
            db.session.commit()

    def get_test_data(self):
        return [
            {
                "total_stats": 200,
                "name": "Magikarp",
                "special_attack": 15,
                "speed": 80,
                "legendary": False,
                "defense": 55,
                "type_2": None,
                "health_points": 20,
                "generation": 1,
                "attack": 10,
                "special_defense": 20,
                "type_1": "Water"
            },
            {
                "total_stats": 195,
                "name": "Caterpie",
                "special_attack": 20,
                "speed": 45,
                "legendary": False,
                "defense": 35,
                "type_2": None,
                "health_points": 45,
                "generation": 1,
                "attack": 30,
                "special_defense": 20,
                "type_1": "Bug"
            },
            {
                "total_stats": 195,
                "name": "Weedle",
                "special_attack": 20,
                "speed": 50,
                "legendary": False,
                "defense": 30,
                "type_2": "Poison",
                "health_points": 40,
                "generation": 1,
                "attack": 35,
                "special_defense": 20,
                "type_1": "Bug"
            },
            {
                "total_stats": 180,
                "name": "Sunkern",
                "special_attack": 30,
                "speed": 30,
                "legendary": False,
                "defense": 30,
                "type_2": None,
                "health_points": 30,
                "generation": 2,
                "attack": 30,
                "special_defense": 30,
                "type_1": "Grass"
            }
        ]

    def test_fetch_pokemon_successfull(self):
        self.create_data()
        response = self.client.get("/pokemon?special_attack__gt=12&special_defense__gt=12&defense__gt=12&attack__gt=10&health_points__gt=20&total_stats__gt=5&speed__gt=10&generation__gt=0&special_attack__lt=100&special_defense__lt=100&defense__lt=100&attack__lt=100&health_points__lt=100&total_stats__lt=200&speed__lt=100&generation__lt=2&order_by=special_attack__asc,special_defense__desc")
        self.assertEqual(200, response.status_code)

        assert_list = self.get_test_data()
        response_list = response.json
        
        for i in range(0, len(assert_list)):
            self.assertEqual(response_list[i], assert_list[i])
