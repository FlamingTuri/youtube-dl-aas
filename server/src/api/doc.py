from src.restx_config import api
from flask_restx import Resource, fields
from flask_restx import Resource, fields
from src.service.doc_service import DocService

ns = api.namespace('youtube-dl', description='Youtube dl documentation')

@ns.route('/doc')
class Doc(Resource):

    doc_service = DocService()

    def get(self):
        return self.doc_service.get_youtube_dl_doc().__dict__
