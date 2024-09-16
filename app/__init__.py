from flask import Flask

from app.routes import auth


def create_app():

    app = Flask(__name__)

    auth.init(app)

    return app
