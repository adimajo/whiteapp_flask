from flask import Flask
from flask_restx import Api
from flask_wtf.csrf import CSRFProtect

from whiteapp.WhiteApp import Version


def create_app():
    """
    Creates the model serving Flask app
    :return: Flask app
    """
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    api = Api(app)
    api.add_resource(Version, '/version')
    csrf = CSRFProtect()
    csrf.init_app(app)

    return app


app = create_app()


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=7000)  # nosec
