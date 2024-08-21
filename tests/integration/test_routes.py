# tests/integration/test_routes.py
import pytest
from app import create_app, db
from app.models import User, Product, Category, Order

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_products(client):
    # Add a sample product to the database
    category = Category(name="Electronics")
    db.session.add(category)
    db.session.commit()
    
    product = Product(
        name="Laptop",
        price=1500.00,
        stock=10,
        category=category
    )
    db.session.add(product)
    db.session.commit()

    response = client.get('/products')
    assert response.status_code == 200
    assert b'Laptop' in response.data  # Verify that the product name appears in the response data


def test_create_product_route(client):
    response = client.post('/products', json={
        "name": "Laptop",
        "price": 1500.00,
        "stock": 10,
        "category_name": "Electronics"
    })
    assert response.status_code == 201
    assert b'Laptop' in response.data  # Verify that the created product is returned in the response

