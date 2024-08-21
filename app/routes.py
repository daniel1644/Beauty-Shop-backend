# routes.py
from flask import Blueprint, request, make_response, jsonify, render_template, session
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from .models import User, Product, Order, Category, OrderItem
from . import db
from .schemas import UserSchema, ProductSchema, CategorySchema, OrderSchema, OrderItemSchema

bcrypt = Bcrypt()

auth_bp = Blueprint('auth', __name__)
product_bp = Blueprint('product', __name__)
order_bp = Blueprint('order', __name__)
admin_bp = Blueprint('admin', __name__)
main_bp = Blueprint('main', __name__)

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
    try:
        data = request.get_json()
        schema = UserSchema()
        result = schema.load(data)
        new_user = User(username=result['username'], email=result['email'], password=result['password'], role=result['role'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify(new_user.to_dict()), 201)
    except ValidationError as err:
        return make_response(jsonify({'error': err.messages}), 400)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)

@auth_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(users)
    return make_response(jsonify(result), 200)

@auth_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    schema = UserSchema()
    result = schema.dump(user)
    return make_response(jsonify(result), 200)

@auth_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    schema = UserSchema()
    result = schema.load(data)
    user.username = result['username']
    user.email = result['email']
    user.role = result['role']
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
    schema = ProductSchema()
    result = schema.load(data)
    category = Category.query.filter_by(name=result['category_name']).first()
    if not category:
        category = Category(name=result['category_name'])
        db.session.add(category)
        db.session.commit()
    
    new_product = Product(
        name=result['name'],
        price=result['price'],
        stock=result['stock'],
        category_id=category.id
    )
    db.session.add(new_product)
    db.session.commit()
    return make_response(jsonify(new_product.to_dict()), 201)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    schema = ProductSchema(many=True)
    result = schema.dump(products)
    return make_response(jsonify(result), 200)

@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    schema = ProductSchema()
    result = schema.dump(product)
    return make_response(jsonify(result), 200)

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    schema = ProductSchema()
    result = schema.load(data)
    product.name = result['name']
    product.price = result['price']
    product.stock = result['stock']
    product.category_id = result['category_id']
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
    schema = CategorySchema()
    result = schema.load(data)
    new_category = Category(name=result['name'])
    db.session.add(new_category)
    db.session.commit()
    return make_response(jsonify(new_category.to_dict()), 201)

@product_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    schema = CategorySchema(many=True)
    result = schema.dump(categories)
    return make_response(jsonify(result), 200)

@product_bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    schema = CategorySchema()
    result = schema.dump(category)
    return make_response(jsonify(result), 200)

@product_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    schema = CategorySchema()
    result = schema.load(data)
    category.name = result['name']
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
    schema = OrderSchema()
    result = schema.load(data)
    user = User.query.get_or_404(result['user_id'])
    new_order = Order(user=user, total_amount=result['total_amount'], status=result['status'])
    db.session.add(new_order)
    db.session.commit()
    return make_response(jsonify(new_order.to_dict()), 201)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    schema = OrderSchema(many=True)
    result = schema.dump(orders)
    return make_response(jsonify(result), 200)

@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    schema = OrderSchema()
    result = schema.dump(order)
    return make_response(jsonify(result), 200)

@order_bp.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    data = request.get_json()
    schema = OrderSchema()
    result = schema.load(data)
    order.status = result['status']
    db.session.commit()
    return make_response(jsonify(order.to_dict()), 200)

@order_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return make_response(jsonify({'message': 'Order deleted successfully'}), 200)





@order_bp.route('/orders/<int:order_id>/items', methods=['POST'])
def create_order_item(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    schema = OrderItemSchema()
    result = schema.load(data)
    product = Product.query.get_or_404(result['product_id'])
    new_order_item = OrderItem(order=order, product=product, quantity=result['quantity'], price=result['price'])
    db.session.add(new_order_item)
    db.session.commit()
    return make_response(jsonify(new_order_item.to_dict()), 201)

@order_bp.route('/orders/<int:order_id>/items', methods=['GET'])
def get_order_items(order_id):
    order = Order.query.get_or_404(order_id)
    order_items = order.items
    schema = OrderItemSchema(many=True)
    result = schema.dump(order_items)
    return make_response(jsonify(result), 200)

@order_bp.route('/orders/<int:order_id>/items/<int:item_id>', methods=['GET'])
def get_order_item(order_id, item_id):
    order = Order.query.get_or_404(order_id)
    order_item = OrderItem.query.get_or_404(item_id)
    schema = OrderItemSchema()
    result = schema.dump(order_item)
    return make_response(jsonify(result), 200)

@order_bp.route('/orders/<int:order_id>/items/<int:item_id>', methods=['PUT'])
def update_order_item(order_id, item_id):
    order = Order.query.get_or_404(order_id)
    order_item = OrderItem.query.get_or_404(item_id)
    data = request.get_json()
    schema = OrderItemSchema()
    result = schema.load(data)
    order_item.quantity = result['quantity']
    order_item.price = result['price']
    db.session.commit()
    return make_response(jsonify(order_item.to_dict()), 200)

@order_bp.route('/orders/<int:order_id>/items/<int:item_id>', methods=['DELETE'])
def delete_order_item(order_id, item_id):
    order = Order.query.get_or_404(order_id)
    order_item = OrderItem.query.get_or_404(item_id)
    db.session.delete(order_item)
    db.session.commit()
    return make_response(jsonify({'message': 'Order item deleted successfully'}), 200)



if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beauty_shop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    bcrypt.init_app(app)
    api = Api(app)
    api.add_resource(Index, '/')
    api.add_resource(UserResource, '/users', '/users/<int:id>')
    api.add_resource(ProductResource, '/products', '/products/<int:id>')
    api.add_resource(CategoryResource, '/categories', '/categories/<int:id>')
    api.add_resource(OrderResource, '/orders', '/orders/<int:id>')
    api.add_resource(OrderItemResource, '/orders/<int:order_id>/items', '/orders/<int:order_id>/items/<int:item_id>')
    app.run(debug=True)