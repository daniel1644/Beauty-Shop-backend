# tests/unit/test_models.py
import pytest
from app.models import User, Product

def test_user_creation():
    user = User(username="testuser", email="test@example.com", password="password")
    assert user.username == "testuser"

def test_product_creation():
    product = Product(name="Sample Product", price=99.99, stock=50)
    assert product.name == "Sample Product"
    assert product.price == 99.99
    assert product.stock == 50
