# -*- coding: utf-8 -*-
from app.core.services.convert_service import ConvertService
from flask import Blueprint, request, jsonify

bp = Blueprint('convert', __name__, url_prefix='/api')

class ConvertController:

    @bp.route('/convert', methods=['GET'])
    def convert_amount():
        '''
            To convert amount according sended currencyCode (optional) or BRL
            (default), returning a map of currencies and converted amounts.
            Params:
                query_param: amount
                query_param: currencyCode (optional)
        '''

        response = ConvertService().service_convert(request)
        if not response:
            return server_error_response_msg()
        return response

