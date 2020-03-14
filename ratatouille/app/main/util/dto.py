from flask_restx import Namespace, fields


class LinkDto:
    api = Namespace("link", description="Links related data")
    link = api.model(
        "link", {"link": fields.String(required=True, description="Link to shorten")}
    )

