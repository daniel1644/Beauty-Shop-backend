#!/usr/bin/env python3

# Standard library imports
import random
from random import randint, sample
from datetime import datetime, timedelta

# Remote library imports
from faker import Faker

# Local imports
from config import config
from app.models import User, Product, Category, Order
from app import create_app, db

fake = Faker()
app = create_app()

with app.app_context():
    # Create tables if they don't exist
    db.create_all()

    print("Deleting all records...")
    Order.query.delete()
    User.query.delete()
    Product.query.delete()
    Category.query.delete()
    db.session.commit()

    print("Creating categories...")

    categories = []
    for _ in range(5):
        category = Category(name=fake.word())
        db.session.add(category)
        categories.append(category)

    print("Creating users...")

    users = []
    for _ in range(5):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
            role=random.choice(['admin', 'customer'])
        )
        db.session.add(user)
        users.append(user)

    print("Creating products...")

    products = []
    for _ in range(20):
        product = Product(
            name=fake.word(),
            description=fake.sentence(),
            price=round(randint(5, 100) + fake.random_number(digits=2), 2),
            stock=randint(1, 100),
            category=random.choice(categories)
        )
        db.session.add(product)
        products.append(product)

    print("Creating orders...")

    orders = []
    for _ in range(10):
        order = Order(
            user=random.choice(users),
            total_amount=round(sum([p.price for p in sample(products, randint(1, 5))]), 2),
            status='pending',  # Provide a default value for the status attribute
            order_date=datetime.now() - timedelta(days=randint(1, 30))
        )
        db.session.add(order)
        orders.append(order)

    db.session.commit()
    print("Complete.")