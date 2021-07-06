from flask import Flask, Response, request

from queries import *
from client import evolve, update_types_for_pokemon
from config import port
app = Flask(__name__)


@app.route('/get_pokemons/<trainer_name>', methods=['GET'])
def get_pokemons_of_trainer(trainer_name):
    res = find_roster(trainer_name)
    return Response("{}".format(res))


@app.route('/get_trainers/<pokemon_name>', methods=['GET'])
def get_trainers_of_pokemon(pokemon_name):
    res = find_owners(pokemon_name)
    return Response("{}".format(res))


@app.route('/new_pokemon', methods=['POST'])
def new_pokemon():  # get params from body
    pokemon_details = request.get_json()
    added = add_pokemon(pokemon_details)
    if added:
        return Response("Added a new pokemon successfully")
    return Response("Addition failed")


@app.route('/pokemon_by_type/<type>', methods=['GET'])
def get_pokemon_by_type(type):
    res = find_by_type(type)
    return Response("{}".format(res))


@app.route('/delete_pokemon/<pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    res = delete_pokemon_sql(pokemon_id)
    return Response("{}".format(res))


@app.route('/update_types/<pokemon_name>', methods=['POST'])
def update_types(pokemon_name):
    res = update_types_for_pokemon(pokemon_name)
    return Response("{}".format(res))


@app.route('/evolve_pokemon/<pokemon_name>/<trainer_name>', methods=['PATCH'])
def evolve_pokemon(pokemon_name, trainer_name):
    succeeded = evolve(pokemon_name, trainer_name)
    if succeeded:
        return Response("Evolved pokemon {} of {} successfully".format(pokemon_name, trainer_name))
    return Response("Evolution failed")


if __name__ == '__main__':
    app.run(port=port)
