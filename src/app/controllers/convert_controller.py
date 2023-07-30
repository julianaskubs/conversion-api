# -*- coding: utf-8 -*-
import logging
from app.core.services.convert_service import ConvertService
from app.core import http_response
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

'''
    Receive an amount and an origin currencyCode(optional - BRL default) to convert,
    according currencies pre-registered on database 
    (the convert only occur in this case)
    
    Params:
        queryStr: amount (required)
        queryStr: currencyCode (optional)
'''

bp = Blueprint('convert', __name__, url_prefix='/api')
convert = ConvertService()


# Get /api/convert?amount=value&currencyCode=value
@bp.route('/convert', methods=['GET'])
def convert_amount():
    try:
        logging.info(
            "[Convert API] Starting to process, request: %s",
            request.query_string.decode('utf-8')
        )
        response = convert.process_handler(request)
        logging.info(
            "[Convert API] Ending to process, response: %s",
            str(response)
        )
        return jsonify(response)

    except BadRequest as ex:
        logging.error(
            "[Convert API] BadRequest: %s",
            ex.description
        )
        return http_response.bad_request_response(ex.description)

    except Exception as e:
        logging.error(
            "[Convert API] An internal server error has occurred while processing request. Error: %s",
            str(e)
        )
        return http_response.server_error_response()
