from flask import Flask, jsonify
import flask_restful as restful
from flask_swagger import swagger
from flask_wtf.csrf import CSRFProtect

try:
    from whiteapp.WhiteApp import Version
    from whiteapp import __version__
except ImportError:
    from WhiteApp import Version
    from . import __version__


def create_app():
    """
    Creates the model serving Flask app
    :return: Flask app
    """
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    api = restful.Api(app)
    api.add_resource(Version, '/')

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = __version__
        swag['info']['title'] = "Data Harvesting"
        return jsonify(swag)

    csrf = CSRFProtect()
    csrf.init_app(app)

    return app


app = create_app()


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)  # nosec
