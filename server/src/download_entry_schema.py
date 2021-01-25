from marshmallow import Schema, fields, post_load

class DownloadEntry:
    def __init__(self, urls, ydlOpts={}):
        self.urls = urls
        self.ydl_opts = ydlOpts


class DownloadEntrySchema(Schema):
    urls = fields.List(fields.String(), required=True)
    ydlOpts = fields.Dict(keys = fields.String(), values = fields.Str(), required = False)

    @post_load
    def make_user(self, data, **kwargs):
        return DownloadEntry(**data)
