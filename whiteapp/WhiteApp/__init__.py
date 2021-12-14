"""
WhiteApp application
"""

from flask_restx import Resource, Namespace, fields
from loguru import logger

from whiteapp import __version__

api = Namespace('')

my_output = api.model("output", {'version': fields.String})


@api.route('/version')
class Version(Resource):
    """
    Flask resource to spit current version
    """
    @api.marshal_with(my_output)
    def get(self):
        logger.debug("Successful GET")
        return {"version": __version__}
