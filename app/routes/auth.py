from flask import Flask, Blueprint, jsonify


auth = Blueprint('auth', __name__)


@auth.route('/auth')
def authenticate():
    return jsonify(msg='Auth route')


def init(app: Flask):
    app.register_blueprint(auth)
