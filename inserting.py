import pymysql
import json

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


def get_data():
    with open("pokemon_data.json") as pokemon_data:
        data = json.load(pokemon_data)
    return data


def insert_to_database():
    data = get_data()
    trainers = []
    for i in data:
        try:
            with connection.cursor() as cursor:
                query1 = 'INSERT INTO pokemon VALUES (%s,%s,%s,%s,%s)'
                values1 = (i["id"], i["name"], i["type"],
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
        except:
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
        print("Error")

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
        print("Error")

        
def finds_most_owned():
    pass

# insert_to_database()
# print(heaviest_pokemon())
# print(find_owners("gengar"))