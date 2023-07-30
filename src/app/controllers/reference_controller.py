# -*- coding: utf-8 -*-
import logging
from flask import jsonify
from app.core.services.reference_service import ReferenceService
from flask import Blueprint
from app.core import http_response

bp = Blueprint('reference', __name__, url_prefix='/api')


# Get /api/references
@bp.route('/references', methods=['GET'])
def get_references():
    try:
        logging.info("[References API] Starting to get currencies information.")
        response = ReferenceService().process_handler()
        logging.info("[References API] Ending to get currencies information.")
        return jsonify(response.get_content())

    except Exception as e:
        logging.error(
            "[References API] An internal server error has occurred while processing request. Error: %s",
            str(e)
        )
        return http_response.server_error_response()
