# -*- coding: utf-8 -*-
import os
from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except Exception as e:
        print(e)

    from .db_connection import db
    db.init_app(app)

    from .controllers import (
        convert_controller,
        currency_controller,
        reference_controller)

    app.register_blueprint(convert_controller.bp)
    app.register_blueprint(currency_controller.bp)
    app.register_blueprint(reference_controller.bp)

    return app
