import connexion
from flask import current_app


def get_server():
    """get the singleton bus of the server application"""
    with current_app.app_context():
        return current_app.server


def list_representations():
    server = get_server()
    return server.list_representations(), 200


def create_representation(body):
    body = connexion.request.get_json()
    args = body.get('args', [])
    kwargs = body.get('kwargs', {})
    server = get_server()
    return server.create_representation(args, kwargs), 200


def upload_representation(body):
    body = connexion.request.get_json()
    args = body.get('args', [])
    kwargs = body.get('kwargs', {})
    server = get_server()
    return server.upload_representation(args, kwargs), 200


def call_representation(representation_uuid, body):
    body = connexion.request.get_json()
    args = body.get('args', [])
    kwargs = body.get('kwargs', {})
    server = get_server()
    return server.call_representation(representation_uuid, args, kwargs), 200


def download_representation(representation_uuid):
    server = get_server()
    return server.download_representation(representation_uuid), 200


def release_representation(representation_uuid):
    server = get_server()
    return server.release_representation(representation_uuid), 200


def create_attribute(representation_uuid, attribute_name):
    server = get_server()
    return server.create_attribute(representation_uuid, attribute_name), 200
