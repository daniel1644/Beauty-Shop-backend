from flask import Blueprint, request, make_response, jsonify, render_template, session
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from .models import User, Product, Order, Category, OrderItem
from . import db

auth_bp = Blueprint('auth', __name__)
product_bp = Blueprint('product', __name__)
order_bp = Blueprint('order', __name__)
admin_bp = Blueprint('admin', __name__)
main_bp = Blueprint('main', __name__)

bcrypt = Bcrypt()

# Define route functions for each Blueprint (auth, product, order, admin)
@main_bp.route("/")
def index():
    return "Welcome to my beauty shop app!"


# @auth_bp.route('/register', methods=['POST'])
# def register():
#     # Handle user registration
#     pass

# @product_bp.route('/products', methods=['GET'])
# def get_products():
#     # Handle fetching all products
#     pass

@auth_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify(new_user.to_dict()), 201)

@auth_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return make_response(jsonify([user.to_dict() for user in users]), 200)

@auth_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return make_response(jsonify(user.to_dict()), 200)

@auth_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    db.session.commit()
    return make_response(jsonify(user.to_dict()), 200)

@auth_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({'message': 'User deleted successfully'}), 200)




@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    category = Category.query.filter_by(name=data['category_name']).first()
    if not category:
        category = Category(name=data['category_name'])
        db.session.add(category)
        db.session.commit()
    
    new_product = Product(
        name=data['name'],
        price=data['price'],
        stock=data['stock'],
        category_id=category.id
    )
    db.session.add(new_product)
    db.session.commit()
    return make_response(jsonify(new_product.to_dict()), 201)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return make_response(jsonify([product.to_dict() for product in products]), 200)

@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return make_response(jsonify(product.to_dict()), 200)

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    product.category_id = data.get('category_id', product.category_id)
    db.session.commit()
    return make_response(jsonify(product.to_dict()), 200)

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return make_response(jsonify({'message': 'Product deleted successfully'}), 200)





@product_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return make_response(jsonify(new_category.to_dict()), 201)

@product_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return make_response(jsonify([category.to_dict() for category in categories]), 200)

@product_bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return make_response(jsonify(category.to_dict()), 200)

@product_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    category.name = data.get('name', category.name)
    db.session.commit()
    return make_response(jsonify(category.to_dict()), 200)

@product_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return make_response(jsonify({'message': 'Category deleted successfully'}), 200)





@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user = User.query.get_or_404(data['user_id'])
    new_order = Order(user=user, total_amount=data['total_amount'], status=data['status'])
    db.session.add(new_order)
    db.session.commit()
    return make_response(jsonify(new_order.to_dict()), 201)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return make_response(jsonify([order.to_dict() for order in orders]), 200)

@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return make_response(jsonify(order.to_dict()), 200)

@order_bp.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    data = request.get_json()
    order.status = data.get('status', order.status)
    db.session.commit()
    return make_response(jsonify(order.to_dict()), 200)

@order_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return make_response(jsonify({'message': 'Order deleted successfully'}), 200)





@order_bp.route('/order_items', methods=['POST'])
def create_order_item():
    data = request.get_json()
    order = Order.query.get_or_404(data['order_id'])
    product = Product.query.get_or_404(data['product_id'])
    new_order_item = OrderItem(order=order, product=product, quantity=data['quantity'], price=data['price'])
    db.session.add(new_order_item)
    db.session.commit()
    return make_response(jsonify(new_order_item.to_dict()), 201)

@order_bp.route('/order_items', methods=['GET'])
def get_order_items():
    order_items = OrderItem.query.all()
    return make_response(jsonify([order_item.to_dict() for order_item in order_items]), 200)

@order_bp.route('/order_items/<int:id>', methods=['GET'])
def get_order_item(id):
    order_item = OrderItem.query.get_or_404(id)
    return make_response(jsonify(order_item.to_dict()), 200)

@order_bp.route('/order_items/<int:id>', methods=['PUT'])
def update_order_item(id):
    order_item = OrderItem.query.get_or_404(id)
    data = request.get_json()
    order_item.quantity = data.get('quantity', order_item.quantity)
    order_item.price = data.get('price', order_item.price)
    db.session.commit()
    return make_response(jsonify(order_item.to_dict()), 200)

@order_bp.route('/order_items/<int:id>', methods=['DELETE'])
def delete_order_item(id):
    order_item = OrderItem.query.get_or_404(id)
    db.session.delete(order_item)
    db.session.commit()
    return make_response(jsonify({'message': 'Order item deleted successfully'}), 200)