from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    role = fields.Str(validate=validate.OneOf(["admin", "customer"]))

class ProductSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2))
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    category_name = fields.Str(required=True)

class OrderSchema(Schema):
    user_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    status = fields.Str(validate=validate.OneOf(["Pending", "Shipped", "Delivered", "Cancelled"]))
