import os
from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config_class)

    create_directory_if_necessary(app.config["UPLOAD_FOLDER"])

    from app.upload import bp as upload_bp
    from app.download import bp as download_bp

    app.register_blueprint(upload_bp)
    app.register_blueprint(download_bp)

    return app


def create_directory_if_necessary(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname, 0o700)
