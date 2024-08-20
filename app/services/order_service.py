from app.models import Order, Product, User
from app import db

class OrderService:
    @staticmethod
    def create_order(user_id, product_id, quantity):
        user = User.query.get(user_id)
        product = Product.query.get(product_id)
        if user and product and product.stock >= quantity:
            new_order = Order(user_id=user.id, product_id=product.id, quantity=quantity, status='Pending')
            product.stock -= quantity
            db.session.add(new_order)
            db.session.commit()
            return new_order
        return None

    @staticmethod
    def get_all_orders():
        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def update_order_status(order_id, status):
        order = Order.query.get(order_id)
        if order:
            order.status = status
            db.session.commit()
            return order
        return None
