from flask_restx import Resource, fields
from src.config.flask_restx_config import api
from src.service.version_service import VersionService

ns = api.namespace('youtube-dl', description='Youtube dl documentation')

doc = api.model(
    "Version",
    {
        "serverVersion": fields.String(required=True, description="Server version"),
        "youtubeDlVersion": fields.String(required=True, description="Youtube dl version"),
    },
)


@ns.route('/version')
class Version(Resource):

    version_service = VersionService()

    @ns.marshal_with(doc)
    def get(self):
        return self.version_service.get_version()
