import uuid
import hashlib

from flask import jsonify

from app.main import db
from app.main.model.link import Link
from app.main.helpers.jsond import to_json


def add_new_link(data):
    link = Link.query.filter_by(url=data["link"]).first()

    if not link:
        longhash = hashlib.sha3_512(str(data["link"]).encode()).hexdigest()
        shorthash = longhash[:3]
        new_link = Link(url=data["link"], longhash=longhash, shorthash=shorthash)
        save_changes(new_link)
        respond_link_obj = to_json(new_link, Link)
        respond_link_obj = eval(respond_link_obj)
        return respond_link_obj, 201
    respond_link_obj = to_json(link, Link)
    respond_link_obj = eval(respond_link_obj)
    return respond_link_obj, 409


def get_url(shorthash):
    link = Link.query.filter_by(shorthash=shorthash).first()
    if not link:
        response_object = {"message": "Not found"}
        return response_object, 404
    respond_link_obj = to_json(link, Link)
    respond_link_obj = eval(respond_link_obj)
    return respond_link_obj, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()

