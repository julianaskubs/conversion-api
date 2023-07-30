# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('healthcheck', __name__, url_prefix='/')


@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'ok'
