from app.models import Product, Category
from app import db

class ProductService:
    @staticmethod
    def create_product(name, price, stock, category_name):
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()
        new_product = Product(name=name, price=price, stock=stock, category_id=category.id)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def update_product(product_id, data):
        product = Product.query.get(product_id)
        if product:
            product.name = data.get('name', product.name)
            product.price = data.get('price', product.price)
            product.stock = data.get('stock', product.stock)
            product.category_id = data.get('category_id', product.category_id)
            db.session.commit()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
