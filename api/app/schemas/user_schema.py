from marshmallow import Schema, fields

class UserSchema(Schema):
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

    email = fields.Email(
        required = True,
        validate = lambda x: "@utma.edu.mx" in x,
        error_messages = {
            "required" : "El email es requerido"
        }
    )

    


