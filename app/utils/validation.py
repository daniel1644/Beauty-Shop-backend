from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6, max=128))
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "customer"]))

class ProductSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    category_name = fields.Str(required=True, validate=validate.Length(min=2, max=50))

class OrderSchema(Schema):
    user_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=1))
    status = fields.Str(required=True, validate=validate.OneOf(["Pending", "Shipped", "Delivered", "Cancelled"]))