from flask_restx import Resource, fields
from src.config.flask_restx_config import api
from src.service.info_service import InfoService

ns = api.namespace('youtube-dl', description='Youtube dl documentation')

doc = api.model(
    'Info', {
        "hostAddress": fields.String(required=True, description="Host address where the server is running")
    }
)


@ns.route('/info')
class Info(Resource):

    info_service = InfoService()

    @ns.marshal_with(doc)
    def get(self):
        return self.info_service.get_host_name()
