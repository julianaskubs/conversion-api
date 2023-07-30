# -*- coding: utf-8 -*-
import logging
from app.core.services.currency_service import CurrencyService
from flask import Blueprint, jsonify, request
from app.core import http_response
from werkzeug.exceptions import BadRequest, NotFound

bp = Blueprint('currency', __name__, url_prefix='/api')


# Post /api/currency - create a new currency (to convert) on database
@bp.route('/currency', methods=['POST'])
def new_currency():
    try:
        logging.info(
            "[Currency API] Starting to process 'Post' request."
        )
        payload = request.json
        CurrencyService().process_handler_post_currency(payload)

        logging.info(
            "[Currency API] Ending to process 'Post' request."
        )
        return http_response.created_response()

    except BadRequest as ex:
        logging.error(
            "[Currency API] BadRequest: %s",
            ex.description
        )
        return http_response.bad_request_response(ex.description)

    except Exception as e:
        logging.error(
            "[Currency API] An internal server error has occurred while processing request. Error: %s",
            str(e)
        )
        return http_response.server_error_response()


# Get or Delete /api/currency/<currency_id> - specify currency from database
@bp.route('/currency/<currency_id>', methods=['GET', 'DELETE'])
def get_currency_by_id(currency_id=None):
    try:
        if request.method == "GET":
            logging.info(
                "[Currency API] Starting to process 'Get' request."
            )
            response = CurrencyService().process_handler_get_currency_by_id(currency_id)

            logging.info(
                "[Currency API] Ending to process 'Get' request."
            )
            return jsonify(response)

        elif request.method == "DELETE":
            logging.info(
                "[Currency API] Starting to process 'Delete' request."
            )
            CurrencyService().process_handler_delete_currency_by_id(currency_id)

            logging.info(
                "[Currency API] Ending to process 'Delete' request."
            )
            return http_response.ok_response()

    except NotFound as exn:
        logging.error(
            "[Currency API] NotFound: %s",
            exn.description
        )
        return http_response.not_found_response(exn.description)

    except Exception as e:
        logging.error(
            "[Currency API] An internal server error has occurred while processing request. Error: %s",
            str(e)
        )
        return http_response.server_error_response()


# Get /api/currencies/ - return all currencies from database
@bp.route('/currencies', methods=['GET'])
def get_currencies():
    try:
        logging.info(
            "[Currency API] Starting to process 'Get all' request."
        )
        response = CurrencyService().process_handler_get_currencies()

        logging.info(
            "[Currency API] Ending to process 'Get all' request."
        )
        return jsonify(response)

    except Exception as e:
        logging.error(
            "[Currency API] An internal server error has occurred while processing request. Error: %s",
            str(e)
        )
        return http_response.server_error_response()
