# # tests/unit/test_models.py
# import pytest
# from app.models import User, Product, Category

# def test_user_creation():
#     user = User(username="testuser", email="test@example.com", password="password", role="customer")
#     assert user.username == "testuser"
#     assert user.email == "test@example.com"
#     assert user.password == "password"
#     assert user.role == "customer"

# def test_product_creation():
#     category = Category(name="Electronics")
#     product = Product(name="Sample Product", price=99.99, stock=50, category=category)
#     assert product.name == "Sample Product"
#     assert product.price == 99.99
#     assert product.stock == 50
#     assert product.category.name == "Electronics"

# def test_category_creation():
#     category = Category(name="Electronics")
#     assert category.name == "Electronics"
