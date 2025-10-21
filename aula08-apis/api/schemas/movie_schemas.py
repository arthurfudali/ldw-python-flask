from api import ma
from marshmallow import fields
class MovieSchema(ma.Schema):
    _id = fields.Str()
    title = fields.Str(required=True)
    description = fields.Str(required=True) 
    duration = fields.Int(required=True)
    director = fields.Str(required=True)
    year = fields.Str(required=True)