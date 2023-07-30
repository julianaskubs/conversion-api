# -*- coding: utf-8 -*-
import cachetools.func
from .external_api import CurrConvAPI
from werkzeug.exceptions import BadRequest


class RequestValidator(object):
    def __init__(self):
        self.payload = None

    def validate_payload(self, body=None):
        """ Validate payload is not empty """
        self.payload = body
        if not self.payload:
            raise BadRequest("An empty payload is not valid.")

        return self.validate_currency_id()

    def validate_currency_id(self):
        """ Validate payload 'currencyId' field """
        if not self.payload.get('currencyId'):
            raise BadRequest("A 'currency_id' attribute should be provided.")

        return self.validate_currency_name()

    def validate_currency_name(self):
        """ Validate payload 'currencyName' """
        if not self.payload.get('currencyName'):
            raise BadRequest("A 'currencyName' attribute should be provided.")

    @staticmethod
    def validate_currency_code(currency: str):
        currencies = get_all_currencies_code()

        if not currencies.get('results', {}).get(currency):
            message = f"Currency Code '{currency}' is invalid. " \
                + "You can search for currencies code in '/api/references/'."
            raise BadRequest(message)


@cachetools.func.ttl_cache(maxsize=10240, ttl=3600)
def get_all_currencies_code():
    try:
        response = CurrConvAPI().get(endpoint='currencies')
        if response.get_status() == 200:
            return response.get_content()

        raise Exception(
            "Bad response from external API:"
            + f" Status Codes {str(response.get_status())}. Message: {str(response.get_content())}"
        )
    except Exception:
        raise
