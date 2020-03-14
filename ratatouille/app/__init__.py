from flask_restx import Api
from flask import Blueprint

from .main.controller.link_controller import api as link_ns

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="", version="beta")

api.add_namespace(link_ns)
