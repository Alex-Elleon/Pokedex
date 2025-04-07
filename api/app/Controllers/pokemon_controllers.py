from flask import Blueprint, jsonify
from app.Models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.Models.factory import ModelFactory

RM = ResponseManager()
bp = Blueprint ("user_Controllers", __name__, url_prefix= "/pokemons")
PM = ModelFactory.get_model("pokemons")
FP_model = ModelFactory.get_model("pokemons")

@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
def get_pokemon(pokemon_id):
    pokemons = PM.find_by_id(ObjectId(pokemon_id))
    return RM.error(pokemons)

@bp.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    data = FP_model.find_all()
    return RM.success(data)
