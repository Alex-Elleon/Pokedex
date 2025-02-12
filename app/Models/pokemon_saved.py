from app import mongo


class Psaved:
    collection = mongo.db.psaveds

    @staticmethod
    def find_all():
        pokemons = Psaved.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemons = Psaved.collection.find_one({
            "_id" : pokemon_id
        })
        return pokemons
    @staticmethod
    def create(data):
        pokemon = Psaved.collection.insert_one(data)
        return pokemon.inserted_id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Psaved.collection.update_one({
            "_id" : pokemon_id
        },
        {
            "$set" : data
        })
        return pokemon

    @staticmethod
    def delete(pokemon_id):
        return Psaved.collection.delete_one({"_id" : pokemon_id})