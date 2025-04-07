#Crea
#Elimina
#Get all
#Especificar a cuales metodos no debe de poder acceder
#Modificar la clase del modelo y evitar que se usen metodos indebidos

from flask import Blueprint, request
from marshmallow import ValidationError
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from app.Models.factory import ModelFactory
from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity 


bp = Blueprint ("favorite_pokemons", __name__, url_prefix="/favorite-pokemons")
RM = ResponseManager()
FP_schema = PokemonFavoriteSchema()
FP_model = ModelFactory.get_model("pokemon_favorites")

@bp.route("/", methods = ["POST"])
@jwt_required()
def create():
        user_id = get_jwt_identity()
        try:
                data = request.json
                data = FP_schema.load(data)
                data["user_id"] = user_id
                fp = FP_model.create(data)
                return RM.success({"_id" : fp})
        except ValidationError as err:
                print(err)
        return RM.error("Es necesario enviar todos los parametros")

@bp.route("/<string:id>", methods = ["DELETE"])
@jwt_required()
def delete(id):
        FP_model.delete(ObjectId(id))
        return RM.success("Pokemon eliminado con exito")

@bp.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = FP_model.find_all(user_id)
    return RM.success(data)