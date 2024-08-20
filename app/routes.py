from flask import Blueprint, request, jsonify, render_template
from .models import User, Product, Order, Category
from . import db

auth_bp = Blueprint('auth', __name__)
product_bp = Blueprint('product', __name__)
order_bp = Blueprint('order', __name__)
admin_bp = Blueprint('admin', __name__)
main_bp = Blueprint('main', __name__)

# Define route functions for each Blueprint (auth, product, order, admin)
# Example:
@main_bp.route("/")
def index():
    return "Welcome to my beauty shop app!"


@auth_bp.route('/register', methods=['POST'])
def register():
    # Handle user registration
    pass

@product_bp.route('/products', methods=['GET'])
def get_products():
    # Handle fetching all products
    pass
