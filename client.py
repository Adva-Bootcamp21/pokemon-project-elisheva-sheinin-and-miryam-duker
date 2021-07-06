import requests
from queries import select_pokemon_id, select_trainer_id, select_trainers, update_pokemon_in_owned_by

def evolve(pokemon_name, trainer_name):
    # try:
        url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_name)
        pokemon_info = requests.get(url, verify=False).json()
        species_url = pokemon_info['species']['url']
        species_info = requests.get(species_url, verify=False).json()
        evolution_chain_url = species_info['evolution_chain']['url']
        evolution_chain_info = requests.get(evolution_chain_url, verify=False).json()
        chain_item = evolution_chain_info['chain']
        current_form = chain_item['evolves_to'][0]
        next_form = current_form['evolves_to'][0]

        while next_form['evolves_to']:
            current_form = next_form[:]
            next_form = current_form['evolves_to'][:]
        evolved_pokemon = current_form['species']['name']

        pokemon_id = select_pokemon_id(pokemon_name)
        trainer_id = select_trainer_id(trainer_name)
        trainers = select_trainers(evolved_pokemon)

        trainers_id = []
        for trainer in trainers:
            trainers_id.append(trainer['trainer_id'])
        if trainer_id not in trainers_id:
            # evolve_values = (
            update_pokemon_in_owned_by(evolved_pokemon, pokemon_id, trainer_id)
        else:
            print("evolved pokemon already exist")
    # except:
    #     print("Error: Failed to update this pokemon of this trainer")

evolve('charmander', 'Jasmine')

# url = 'https://pokeapi.co/api/v2/pokemon/{}'.format('charmander')
# pokemon_info = requests.get(url, verify=False).json()
# url = 'https://pokeapi.co/api/v2/pokemon/{}'.format('charmander')
# pokemon_info = requests.get(url, verify=False)
# a=pokemon_info.json()



# url = 'https://pokeapi.co/api/v2/pokemon/{}'.format('charmander')
# pokemon_info = requests.get(url, verify=False)
# a=pokemon_info.json()