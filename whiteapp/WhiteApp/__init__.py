"""
WhiteApp application
"""

from flask.json import jsonify
from flask_restful import Resource
from loguru import logger

try:
    from whiteapp import __version__
except ImportError:
    import sys
    sys.path.append("..")
    from whiteapp import __version__


class Version(Resource):
    """
    Flask resource to spit current version
    """
    def get(self):
        """
        get method for Version resource: outputs the current version of the whiteapp.
        ---
        responses:
            200:
                description: version of the whiteapp
            400:
                description: successfully POSTed but failed to JSONify API version
            500:
                description: all other server errors
        """
        logger.info("Successful GET")

        try:
            response = jsonify({"version": __version__})
            response.status_code = 200
        except:
            response = jsonify("API failed")
            response.status_code = 400
        logger.info("Successfully JSONified result")

        return response
