from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import AuthService

def get_current_user():
    user_id = get_jwt_identity()
    return AuthService.get_user_by_id(user_id) if user_id else None

def jwt_required_for_role(role):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user = get_current_user()
            if current_user and current_user.role == role:
                return fn(*args, **kwargs)
            return {'error': 'Access denied'}, 403
        return decorator
    return wrapper