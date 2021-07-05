from flask import Flask, Response, request

from queries import *

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
    # find_by_type(type)
    pass


@app.route('/delete_pokemon/<pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    res = delete_pokemon_sql(pokemon_id)
    return Response("{}".format(res))


if __name__ == '__main__':
    app.run(port=5000)