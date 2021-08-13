# -*- coding: utf-8 -*-
from app.core.external_reference_api import ExternalReferenceAPI
from app.core.response import *
from app.data import queries
from .currency_service import CurrencyService
from app.core.currency_validator import CurrencyValidator
from db_connection.db import get_db, close_db
from flask import request
import json
import requests

DEFAULT_CURRENCY = 'BRL'

class ConvertService:

    def service_convert(self, request):
        status_code = 400
        result = dict()

        try:
            amount = request.args.get('amount', None)
            if not amount:
                return create_response_msg(
                    "An 'amount' query string should be provided.",
                    400
                )

            currency_from = request.args.get('currencyCode', None)

            if currency_from and currency_from != DEFAULT_CURRENCY:
                is_valid, message = CurrencyValidator().validate_currency_code(
                    currency_from)

                if not is_valid:
                    if not message:
                        return server_error_response_msg()
                    return create_response_msg(message, status_code)
            else:
                currency_from = DEFAULT_CURRENCY

            # get currencies from database
            db_currencies = CurrencyService().service_get_currencies()

            for c in db_currencies['results']:
                currency_id = c.get('currencyId')
                # external_reference_api
                converted_amount = self.convert_amount_to_currency(
                    amount,
                    currency_from,
                    currency_id)

                if not converted_amount:
                    break
                    return server_error_response_msg()

                result[currency_id] = converted_amount

            return jsonify(dict(results=result))

        except Exception as e:
            print(e)
        return server_error_response_msg()


    def convert_amount_to_currency(self, amount, currency_from, currency_to):
        try:
            endpoint = 'convert'
            convert_key= f'{currency_to}_{currency_from}'
            params = f"q={convert_key}"

            api = ExternalReferenceAPI()
            response = api.get(endpoint, params)

            if response:
                conversion_rate = response.get_content().get(convert_key)
                return self.get_converted_amount(
                    amount,
                    conversion_rate)

        except Exception as e:
            print(e)
        return None


    def get_converted_amount(self, amount: str, conversion_rate: float):
        try:
            amount = float(amount)/100
            result = round(amount * conversion_rate, 2)
            return "{:,.2f}".format(result).replace(",", "X").replace(".", ",").replace("X", ".")
        except Exception as e:
            print(e)
        return None
