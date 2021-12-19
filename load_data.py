import argparse
import pandas as pd
from app import db
from models.pokemon import Pokemon

class LoadDataController:
    
    def __init__(self, file_path):
        self.db_session = db.session
        self.file_path = file_path

    def run_process(self):
        data = pd.read_csv(self.file_path)

        for index, row in data.T.iteritems():
            pokemon = Pokemon()
            pokemon.name = row[1]
            pokemon.type_1 = row[2]
            pokemon.type_2 = row[3]
            pokemon.total_stats = row[4]
            pokemon.health_points = row[5]
            pokemon.attack = row[6]
            pokemon.defense = row[7]
            pokemon.special_attack = row[8]
            pokemon.special_defense = row[9]
            pokemon.speed = row[10]
            pokemon.generation = row[11]
            pokemon.legendary = row[12]

            self.db_session.add(pokemon)
        
        self.db_session.commit()

def get_parameters():
    parser = argparse.ArgumentParser("load_data")
    parser.add_argument("--file_path", required=True)

    args = parser.parse_args()
    return vars(args)

if __name__ == "__main__":
    try:
        params = get_parameters()
        process = LoadDataController(**params)
        process.run_process()
    except IndexError as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e