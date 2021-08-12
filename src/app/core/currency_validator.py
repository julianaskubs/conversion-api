# -*- coding: utf-8 -*-

class CurrencyValidator:

    def __init__(self, payload):
        self.payload = payload

    def validate_payload(self):
        """ Validate payload is not empty """
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