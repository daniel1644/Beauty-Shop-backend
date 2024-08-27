from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import db

class AuthService:
    @staticmethod
    def register_user(username, email, password, role="customer"):
        if User.query.filter_by(email=email).first():
            return None  # User with this email already exists
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return access_token, user
        return None, None

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)