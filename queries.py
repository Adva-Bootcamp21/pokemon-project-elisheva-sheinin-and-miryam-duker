import pymysql
import json
import requests

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def get_data_from_json():
    with open("pokemon_data.json") as pokemon_data:
        data = json.load(pokemon_data)
    return data


def get_data_from_API():
    data = requests.get('https://pokeapi.co/api/v2')
    return data


def get_type_id():
    with connection.cursor() as cursor:
        cursor.execute('''SELECT COUNT(*)
                        FROM types''')
        result = cursor.fetchall()
    return result + 1

def insert_to_database():
    data = get_data_from_json()
    trainers = []

    for i in data:
        # try:
        with connection.cursor() as cursor:
            query1 = 'INSERT INTO pokemon VALUES (%s,%s,%s,%s)'
            values1 = (i["id"], i["name"],
                       i["height"], i["weight"])
            cursor.execute(query1, values1)
            connection.commit()
            query2 = 'INSERT INTO trainer VALUES (%s,%s,%s)'
            query3 = 'INSERT INTO owned_by VALUES (%s,%s)'
            for j in i["ownedBy"]:
                if j not in trainers:
                    trainers.append(j)
                    trainer_id = len(trainers)
                    values2 = (trainer_id, j["name"], j["town"])
                    cursor.execute(query2, values2)
                    connection.commit()
                else:
                    counter = 1
                    for trainer in trainers:
                        if trainer == j:
                            trainer_id = counter
                            break
                        counter += 1
                values3 = (i["id"], trainer_id)
                cursor.execute(query3, values3)
                connection.commit()
        # except:
        print("Error")


def heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT name AS heaviest 
                            FROM pokemon 
                            WHERE weight = (
                                SELECT MAX(weight) 
                                FROM pokemon)''')
            result = cursor.fetchall()
            return result[0]['heaviest']
    except:
        print("Error: Failed to select the heaviest pokemon")


def find_by_type(type):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT name 
                    FROM pokemon p, types t 
                    WHERE p.pokemon_id = t.pokemon_id 
                    AND t.type = (%s)''', type)
            pokemons = cursor.fetchall()
            pokemons_names = []
            for i in pokemons:
                pokemons_names.append(i['name'])
            return pokemons_names
    except:
        print("Error: Failed to find pokemon by type")


def find_owners(pokemon_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT t.name 
                            FROM pokemon p, owned_by o, trainer t 
                            WHERE p.id = o.pokemon_id 
                            AND t.id = o.trainer_id 
                            AND p.name = %s''', pokemon_name)
            result = cursor.fetchall()
            name_list = []
            for name in result:
                name_list.append(name['name'])
            return name_list
    except:
        print("Error: Failed to find owners to this pokemon")


def find_roster(trainer_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT id 
                            FROM trainer 
                            WHERE name = (%s)'''
                            ,trainer_name)
            trainer_id = cursor.fetchall()[0]['id']
            cursor.execute('''SELECT pokemon_id 
                            FROM owned_by 
                            WHERE trainer_id = (%s)'''
                            , trainer_id)
            pokemon_ids = cursor.fetchall()
            pokemons = []
            for i in pokemon_ids:
                cursor.execute('''SELECT name 
                                FROM pokemon 
                                WHERE id = (%s)'''
                                , i['pokemon_id'])
                pokemons.append(cursor.fetchone())
            pokemon_names = []
            for i in pokemons:
                pokemon_names.append(i['name'])
            return pokemon_names

    except:
        print("error")


def finds_most_owned():
    try:
        with connection.cursor() as cursor:
            cursor.execute('''SELECT pokemon_id
                            FROM (
                            SELECT pokemon_id, COUNT(*) as count
                            FROM owned_by
                            GROUP BY pokemon_id) as A
                            WHERE count >= ALL(SELECT  COUNT(*)
                            FROM owned_by
                            GROUP BY pokemon_id)''')
            result = cursor.fetchall()
            most_owned = []
            for pokemon in result:
                most_owned.append(pokemon['pokemon_id'])
            return most_owned
    except:
        print("error")


def add_pokemon(pokemon):
    try:
        with connection.cursor() as cursor:
            query = 'INSERT INTO pokemon VALUES (%s,%s,%s,%s)'
            values = (pokemon["id"], pokemon["name"],
                      pokemon["height"], pokemon["weight"])
            cursor.execute(query, values)
            connection.commit()
            for type in pokemon["types"]:
                cursor.execute('''SELECT id 
                                FROM types
                                WHERE type = %s'''
                               , type)
                result = cursor.fetchall()
                type_id = get_type_id()
                if result == 'no data':
                    type_query = 'INSERT INTO types values(%s, %s)'
                    type_values = (type_id, type)
                    cursor.execute(type_query, type_values)
                has_type_query = 'INSERT INTO has_types values(%s, %s)'
                has_type_values = (pokemon["id"], type_id)
                cursor.execute(has_type_query, has_type_values)

            return True
    except:
        print("error")
        return False


def delete_pokemon_sql(pokemon_id):
    try:
        with connection.cursor() as cursor:
            query = 'DELETE FROM pokemon WHERE id = (%s)'
            values = (pokemon_id)
            cursor.execute(query, values)
            connection.commit()
            return "Deleted pokemon successfully"
    except:
        print("error")


insert_to_database()
