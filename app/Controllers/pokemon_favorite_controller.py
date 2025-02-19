#Crea
#Elimina
#Get all
#Especificar a cuales metodos no debe de poder acceder
#Modificar la clase del modelo y evitar que se usen metodos indebidos

from flask import Blueprint, jsonify
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from app.Models.factory import ModelFactory
from bson import ObjectId 


bp = Blueprint ("pokemon_favorite", __name__, url_prefix= "/pokemon_favorite")
pokemon_schema = PokemonFavoriteSchema()
pokemon_favorites_model = ModelFactory.get_model("pokemon_favorite")

@bp.route("/create/<string:pokemon_id>", methods = ["CREATE"])
def create(pokemon_id):
        pokemon_favorites_model.create(ObjectId(pokemon_id))
        return jsonify("Los parametros enviados son incorrectos", 400)

@bp.route("/delete/<string:pokemon_id>", methods = ["DELETE"])
def delete(pokemon_id):    
        pokemon_favorites_model.delete(ObjectId(pokemon_id))
        return jsonify("Los parametros enviados son incorrectos", 400)

@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
def get_all(pokemon_id):
        pokemon = pokemon_favorites_model.find_by_id(ObjectId(pokemon_id))
        return jsonify("Los parametros enviados son incorrectos", 400)