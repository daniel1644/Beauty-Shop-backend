# # tests/unit/test_product_service.py
# import pytest
# from app.models import Product, Category
# from app.services import ProductService
# from app import db

# def test_create_product():
#     category = Category(name="Electronics")
#     db.session.add(category)
#     db.session.commit()

#     product = ProductService.create_product("Laptop", 1500.00, 10, "Electronics")
#     assert product.name == "Laptop"
#     assert product.price == 1500.00
#     assert product.stock == 10
#     assert product.category.name == "Electronics"

# def test_get_product_by_id():
#     category = Category(name="Electronics")
#     db.session.add(category)
#     db.session.commit()

#     product = ProductService.create_product("Laptop", 1500.00, 10, "Electronics")
#     fetched_product = ProductService.get_product_by_id(product.id)
#     assert fetched_product.id == product.id
#     assert fetched_product.name == "Laptop"
