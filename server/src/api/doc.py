from flask_restx import Resource, fields
from src.config.flask_restx_config import api, ns
from src.service.doc_service import DocService

doc = api.model(
    "Doc",
    {
        "content": fields.String(required=True, description="Documentation returned by Youtube dl library"),
    },
)


@ns.route('/doc')
class Doc(Resource):

    doc_service = DocService()

    @ns.marshal_with(doc)
    def get(self):
        return self.doc_service.get_youtube_dl_doc()
