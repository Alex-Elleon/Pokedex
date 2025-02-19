from flask import Blueprint, jsonify
from app.Models.factory import ModelFactory
from bson import ObjectId 


bp = Blueprint ("pokemons", __name__, url_prefix= "/pokemons")
pokemon_model = ModelFactory.get_model("pokemons")

@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
def get_pokemon(pokemon_id):
        
        pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
        return jsonify("Los parametros enviados son incorrectos", 400)