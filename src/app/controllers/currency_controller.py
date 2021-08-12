# -*- coding: utf-8 -*-
from src.app.core.services.currency_service import CurrencyService
from flask import Blueprint, request
from src.app.core.response import *

bp = Blueprint('currency', __name__, url_prefix='/api')

class CurrencyController:

    @bp.route('/currency', methods=['POST'])
    def new_currency():
        '''
            Create a currency tuple in the database
            Payload:
                str<currencyId>
                str<currencyName>
        '''
        try:
            payload = request.json
        except:
            payload = []
        response = CurrencyService().service_post_currency(payload)
        if not response:
            return server_error_response_msg()
        return response


    @bp.route('/currency/<currency_id>', methods=['GET', 'DELETE'])
    def get_currency_by_id(currency_id=None):

        if request.method == "GET":
            '''
                Return saved informations about the currency from database
                Params: currency_id
            '''
            response = CurrencyService().service_get_currency_by_id(currency_id)
            if not response:
                return server_error_response_msg()
            return response

        if request.method == "DELETE":
            '''
                Delete saved currency from database
                Params: currency_id
            '''
            response = CurrencyService().service_delete_currency_by_id(currency_id)
            if not response:
                return server_error_response_msg()
            return response


    @bp.route('/currencies', methods=['GET'])
    def get_currencies():
        '''
            Create a currency tuple in the database
            Payload:
                str<currency_id>
                str<currency_name>
        '''
        response = CurrencyService().service_get_currencies()
        # if not isinstance(response, list):
        if not response:
            return server_error_response_msg()
        return response
