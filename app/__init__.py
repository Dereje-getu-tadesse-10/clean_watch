
from flask import Flask
from .routes import index


def App():
    app = Flask(__name__)

    app.register_blueprint(index.bp)

    return app
