# autolab

To generate a new database with its structure please execute

flask db upgrade

it will execute every migration

after this run the command

python -m load_data --file_path=pokemon.csv

to run the application execute

python run.py

To get pokemons please use postman to easier finding or throught browser give query params