# # tests/integration/test_routes.py
# import pytest
# from app import create_app, db
# from app.models import User, Product, Category, Order

# @pytest.fixture
# def client():
#     app = create_app()
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()
#         yield client
#         with app.app_context():
#             db.drop_all()

# def test_get_products(client):
#     # Add a sample product to the database
#     category = Category(name="Electronics")
#     db.session.add(category)
#     db.session.commit()
    
#     product = Product(
#         name="Laptop",
#         price=1500.00,
#         stock=10,
#         category_id=category.id
#     )
#     db.session.add(product)
#     db.session.commit()

#     response = client.get('/products')
#     assert response.status_code == 200
#     assert b'Laptop' in response.data  # Verify that the product name appears in the response data

# def test_create_product(client):
#     response = client.post('/products', json={
#         "name": "Laptop",
#         "price": 1500.00,
#         "stock": 10,
#         "category_name": "Electronics"
#     })
#     assert response.status_code == 201
#     assert b'Laptop' in response.data  # Verify that the created product is returned in the response

# def test_create_user(client):
#     response = client.post('/users', json={
#         "username": "testuser",
#         "email": "test@example.com",
#         "password": "password",
#         "role": "customer"
#     })
#     assert response.status_code == 201
#     assert b'testuser' in response.data  # Verify that the created user is returned in the response

# def test_get_users(client):
#     # Add a sample user to the database
#     user = User(username="testuser", email="test@example.com", password="password", role="customer")
#     db.session.add(user)
#     db.session.commit()

#     response = client.get('/users')
#     assert response.status_code == 200
#     assert b'testuser' in response.data  # Verify that the user appears in the response data

# def test_get_user(client):
#     # Add a sample user to the database
#     user = User(username="testuser", email="test@example.com", password="password", role="customer")
#     db.session.add(user)
#     db.session.commit()

#     response = client.get(f'/users/{user.id}')
#     assert response.status_code == 200
#     assert b'testuser' in response.data  # Verify that the user data is correctly returned

# def test_update_user(client):
#     # Add a sample user to the database
#     user = User(username="testuser", email="test@example.com", password="password", role="customer")
#     db.session.add(user)
#     db.session.commit()

#     response = client.put(f'/users/{user.id}', json={
#         "username": "updateduser",
#         "email": "updated@example.com"
#     })
#     assert response.status_code == 200
#     assert b'updateduser' in response.data  # Verify that the user data is correctly updated

# def test_delete_user(client):
#     # Add a sample user to the database
#     user = User(username="testuser", email="test@example.com", password="password", role="customer")
#     db.session.add(user)
#     db.session.commit()

#     response = client.delete(f'/users/{user.id}')
#     assert response.status_code == 200
#     assert b'User deleted successfully' in response.data  # Verify that the user is deleted successfully
