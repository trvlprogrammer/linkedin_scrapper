from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager


jwt = JWTManager()


def api_response(status,message,data):
    return {
        "status" : status,
        "message" : message,
        "data" : data
    }


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt.init_app(app)


    from apps.api import bp as api_bp
    app.register_blueprint(api_bp,url_prefix='/api')


    return app


