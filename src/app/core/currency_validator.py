# -*- coding: utf-8 -*-
from .external_reference_api import ExternalReferenceAPI

class CurrencyValidator(object):

    def __init__(self):
        self.payload = None
        self.currencies = None


    def validate_payload(self, p):
        """ Validate payload is not empty """
        self.payload = p
        if not self.payload:
            return (False, "An empty payload is not valid.")
        return self.validate_id()


    def validate_id(self):
        """ Validate payload 'currencyId' field """
        if not self.payload.get('currencyId'):
            return (False, "A 'currency_id' attribute should be provided.")

        return self.validate_name()


    def validate_name(self):
        """ Validate payload 'currencyName' """

        if not self.payload.get('currencyName'):
            return (False, "A 'currencyName' attribute should be provided.")

        return (True, 'ok')


    def validate_currency_code(self, currency: str):
        try:
            message = "Try to search the correct code in '/api/references/'."

            if self.currencies:
                if self.currencies.get('results').get(currency):
                    return (True, None)
                return (
                    False,
                    f"Currency Code '{currency}' is invalid. " + message)

            endpoint = 'currencies'
            api = ExternalReferenceAPI()
            response = api.get(endpoint)

            if response:
                content = response.get_content()
                if content.get('results').get(currency):
                    self.currencies = content
                    return (True, None)

                return (
                    False,
                    f"Currency Code '{currency}' is invalid. " + message)

        except Exception as e:
            print(e)

        return (False, None)
