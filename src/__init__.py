from flask import Flask
from dotenv import load_dotenv
from .models import db, bcrypt
from flask_jwt_extended import JWTManager
from .auth import jwt

def create_app():

    load_dotenv()
    
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    jwt.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    print(f"Current Key: {app.config.get('SECRET_KEY')}")
    print(f"Using Database: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    print(f"Secret: {app.config.get('JWT_SECRET_KEY')}")
    
    from . import routes
    from . import auth

    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    
    return app