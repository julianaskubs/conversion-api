# -*- coding: utf-8 -*-
import logging
import cachetools.func
from app.settings import *
from app.core.external_api import CurrConvAPI
from .currency_service import CurrencyService
from app.core.req_validator import RequestValidator
from werkzeug.exceptions import BadRequest


class ConvertService(object):
    def process_handler(self, req) -> dict:
        amount = req.args.get('amount', None)
        if not amount:
            raise BadRequest("An 'amount' queryStr param should be provided.")

        currency_from = req.args.get('currencyCode', DEFAULT_CURRENCY)

        logging.info(
            "Processing: amount: %s, currency: %s", amount, currency_from
        )

        if currency_from and currency_from != DEFAULT_CURRENCY:
            self.validate_currency(currency_from)

        result = dict()

        logging.info(
            "Getting currencies (pre-registered) from database"
        )
        db_currencies = CurrencyService().process_handler_get_currencies()

        for c in db_currencies['results']:
            currency_id = c.get('currencyId')

            logging.info(
                "Calling external API to convert currency: %s,", currency_id
            )
            converted_amount = self.convert_amount_to_currency(
                amount,
                currency_from,
                currency_id
            )

            result[currency_id] = "{:,.2f}".format(
                converted_amount).replace(
                    ",", "X").replace(
                    ".", ",").replace("X", ".")

        logging.info(
            "Finished request processing. Result: %s", str(result)
        )
        return dict(results=result)

    @staticmethod
    def validate_currency(currency_from):
        RequestValidator().validate_currency_code(currency_from)

    @cachetools.func.ttl_cache(maxsize=10240, ttl=600)
    def convert_amount_to_currency(self, amount, currency_from, currency_to):
        try:
            convert_key = f'{currency_from}_{currency_to}'
            params = f"q={convert_key}"

            response = CurrConvAPI().get(endpoint='convert', query_str=params)

            if response.get_status() == 200:
                conversion_rate = response.get_content().get(convert_key)
                return self.convert(
                    amount,
                    conversion_rate)
            else:
                raise Exception(
                    "Bad response from external API:"
                    + f" Status Codes {str(response.get_status())}. Message: {str(response.get_content())}"
                )
        except Exception:
            raise

    @staticmethod
    def convert(initial_amount: str, factor: float) -> float:
        try:
            initial_amount = float(initial_amount) / 100
            return round(initial_amount * factor, 2)
        except Exception:
            raise
