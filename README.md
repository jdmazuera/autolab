# Autolab Flask Test

## Setup Project

<p>To generate a new database with its structure please execute</p>

**flask db upgrade**

<p>After please run the command, it will load data of pokemons from csv file to the database</p>

**python -m scripts.load_data --file_path=pokemon.csv**

<p>To create a user please execute the command, it will create a user with username as admin 
and password as admin you can change this values if you want</p>

**python -m scripts.create_user --username=admin --password=admin**
## Execute the application

<p>To execute the application execute the command</p>

**python run.py**

## Using Pokemon API

<p>To fetch data from pokemon endpoint you must have a valid token, to fetch one you should request this 
endpoint first, you can use postman</p>

**http://localhost:5000/auth?username=admin&password=admin**

<p>Set the token from the previous token in Bearer Token option for Authorization in Postman and
set the filters to get your desired pokemons</p>

**http://localhost:5000/pokemon?name=Bulvasaur**

## Filters

<p>You can search pokemons setting the exact values for the desired pokemon or you can set range of data
for integer fields to look for several pokemons. All the string parameters will be treated as like filters
and every integer field has __gt and __lt options to look for ranges I.E</p>

**http://localhost:5000/pokemon?special_attack__gt=12&special_defense__gt=12&defense__gt=12&attack__gt=10&health_points__gt=20&total_stats__gt=5&speed__gt=10&generation__gt=0&special_attack__lt=100&special_defense__lt=100&defense__lt=100&attack__lt=100&health_points__lt=100&total_stats__lt=200&speed__lt=100&generation__lt=2**