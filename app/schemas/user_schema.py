from marshmallow import Schema, fields, ValidationError

class UserSchem(Schema):
    name = fields.Str(
        required = True,
        validate = lambda x: len(x) >0,
        error_messages = {
            "required" : "El nombre es requerido"
        }
    )

    password = fields.Str(
        required = True,
        validate = lambda x: len(x) >0,
        error_messages = {
            "required" : "El contrseña es requerido"
        }
    )

    email = fields.Str(
        required = True,
        validate = lambda x: "@utma.edu.mx" in x,
        error_messages = {
            "required" : "El email es requerido"
        }
    )

    


