from marshmallow import Schema, fields, ValidationError, pre_load


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    first_name = fields.String()
    last_name = fields.String()
    phone = fields.String()


class PasswordSchema(Schema):
    pass_id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    url = fields.Url(required=True)
    title = fields.String()
    login = fields.String(required=True)
    password = fields.String(required=True)
    comment = fields.String()
