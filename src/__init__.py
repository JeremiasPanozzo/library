from flask import Flask
from . import routes
from dotenv import load_dotenv
from .models import db

def create_app():

    load_dotenv()
    
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    # print(f"Current Environment: {app.config.get('SECRET_KEY')}")
    # print(f"Using Database: {app.config.get('DATABASE')}")
    
    app.register_blueprint(routes.bp)

    return app