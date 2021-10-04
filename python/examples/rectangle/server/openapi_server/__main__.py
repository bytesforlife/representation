#!/usr/bin/env python3

import connexion

from flask import current_app

from openapi_server import encoder
from server import Server


def main():
    app = connexion.App(__name__, specification_dir='openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'representation'},
                pythonic_params=True)

    with app.app.app_context():
        current_app.server = Server()

    app.run(port=8080)


if __name__ == '__main__':
    main()
