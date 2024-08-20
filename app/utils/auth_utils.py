from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import AuthService

def get_current_user():
    user_id = get_jwt_identity()
    if user_id:
        return AuthService.get_user_by_id(user_id)
    return None

def jwt_required_for_role(role):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            user = get_current_user()
            if user and user.role == role:
                return fn(*args, **kwargs)
            return {'message': 'Access denied'}, 403
        return decorator
    return wrapper
