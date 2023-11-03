from flask import Flask
from extenssions import db


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    db.init_app(app)
    return app
