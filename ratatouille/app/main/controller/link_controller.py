import logging

from flask import request
from flask_restx import Resource

from ..util.dto import LinkDto
from ..services.link_service import add_new_link, get_url

api = LinkDto.api
_link = LinkDto.link


@api.route("/")
class LinkResource(Resource):
    @api.doc("Get full Link object")
    @api.response(200, "Link is found")
    @api.response(404, "Link is not found")
    def get(self):
        return get_url(request.args["hash"])

    @api.response(201, "Short link created")
    @api.response(409, "Url is already present")
    @api.doc("Create new short url")
    def post(self):
        """Creates new link"""
        data = request.json
        return add_new_link(data=data)
