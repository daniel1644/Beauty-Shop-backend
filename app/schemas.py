from marshmallow import Schema, fields, validate, validates, ValidationError
from app.models import User, Product, Order, Category, OrderItem

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True, validate=validate.Length(max=100))
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates('username')
    def validate_username(self, value):
        if User.query.filter_by(username=value).first():
            raise ValidationError("Username is already taken.")

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    description = fields.Str(required=True, validate=validate.Length(min=10, max=500))
    price = fields.Float(required=True, validate=validate.Range(min=0.01))
    stock = fields.Int(required=True, validate=validate.Range(min=0))
    category_id = fields.Int(required=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=80))

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    total_amount = fields.Float(dump_only=True)
    status = fields.Str(required=True, validate=validate.OneOf(["Pending", "Shipped", "Delivered", "Cancelled"]))
    order_date = fields.DateTime(dump_only=True)
    items = fields.List(fields.Nested('OrderItemSchema'), dump_only=True)  # Nested order items

class OrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0.01))