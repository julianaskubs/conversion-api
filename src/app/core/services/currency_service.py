# -*- coding: utf-8 -*-
from app.core.currency_validator import CurrencyValidator
from app.core.response import *
from app.data import queries
from db_connection.db import get_db, close_db
import json
import requests

class CurrencyService:

    def service_get_currency_by_id(self, currency_id):
        try:
            db = get_db()
            row = db.execute(queries.CURRENCY_BY_ID, (currency_id,)
                ).fetchone()
            close_db()

            if row is None:
                return create_response_msg(
                    f"Currency '{currency_id}' not found.",
                    requests.codes.not_found)

            currency_str = json.dumps(dict(row))
            return json.loads(currency_str)

        except Exception as e:
            close_db()
            print(e)
            return server_error_response_msg()


    def service_delete_currency_by_id(self, currency_id):
        try:
            db = get_db()
            db.execute(queries.DEL_CURRENCY_BY_ID, (currency_id,))
            db.commit()
            close_db()
            return create_response_msg('ok', requests.codes.ok)

        except Exception as e:
            close_db()
            print(e)
            return server_error_response_msg()


    def service_get_currencies(self):
        try:
            db = get_db()
            rows = db.execute(queries.CURRENCIES).fetchall()
            close_db()
            currencies_str = json.dumps([dict(x) for x in rows])
            currencies = json.loads(currencies_str)
            return dict(results=currencies)

        except Exception as e:
            close_db()
            print(e)
            return server_error_response_msg()

    def service_post_currency(self, payload):
        try:
            if isinstance(payload, dict):
                payload_list = []
                payload_list.append(payload)
                payload = payload_list

            catch_error = self.check_payload(payload)
            if catch_error:
                return catch_error

            is_created = self.create_currencies(payload)
            if not is_created:
                return server_error_response_msg()

            return create_response_msg('ok', requests.codes.created)

        except Exception as e:
            print(e)
            return server_error_response_msg()


    def create_currencies(self, payload=[]):
        try:
            db = get_db()
            for p in payload:
                db.execute(
                    queries.CREATE_CURRENCY, (
                        p['currencyId'], p['currencyName'],)
                )
                db.commit()
            close_db()
            return True

        except Exception as e:
            close_db()
            print(e)
            return None


    def check_payload(self, payload):
        status_code = 400
        message = None

        if not isinstance(payload, list):
            return create_response_msg(
                'Payload must be a dict or a list of dict format',
                status_code)

        validator = CurrencyValidator()
        for p in payload:

            # validate currency code
            is_valid, message = validator.validate_currency_code(
                p['currencyId'])

            # validate payload
            if is_valid:
                is_valid, message = validator.validate_payload(p)

            # validate unique fields
            if is_valid:
                is_valid, message = self.validate_unique_fields(
                    p['currencyId'], p['currencyName'])

            if not is_valid:
                if not message:
                    return server_error_response_msg()
                return create_response_msg(message, status_code)

        return None


    def validate_unique_fields(self, currency_id: str, currency_name: str):
        try:
            db = get_db()

            if db.execute(
                queries.CURRENCY_BY_ID, (currency_id,)
            ).fetchone() is not None:
                close_db()
                return (
                    False,
                    f"Already exist a currencyId '{currency_id}' registered.")

            if db.execute(
                queries.CURRENCY_BY_NAME, (currency_name,)
            ).fetchone() is not None:
                close_db()
                return (
                    False,
                    f"Already exist a currencyName '{currency_name}' registered.")

        except Exception as e:
            close_db()
            print(e)
            return (False, None)


        close_db()
        return (True, None)
