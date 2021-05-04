from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from app.main.controller import bp as main_bp
    app.register_blueprint(main_bp)
    return app
'''
    from app.download_file import bp as download_file_bp
    app.register_blueprint(download_file_bp)
'''


'''
from app import model, forms
from app import NV_so_11
'''