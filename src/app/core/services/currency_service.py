# -*- coding: utf-8 -*-
import logging
import json
from app.core.req_validator import RequestValidator
from app.data import queries
from db_connection.db import get_db, close_db
from werkzeug.exceptions import BadRequest, NotFound


class CurrencyService:

    def process_handler_post_currency(self, payload):
        try:
            if isinstance(payload, dict):
                payload_list = [payload]
                payload = payload_list

            self._payload_validations(payload)

            self._create_currencies(payload)

        except Exception:
            raise

    @staticmethod
    def process_handler_get_currency_by_id(currency_id):
        try:
            logging.info("Open db connection.")
            db = get_db()
            row = db.execute(queries.CURRENCY_BY_ID, (currency_id,)).fetchone()

            logging.info("Close db connection.")
            close_db()

            if row is None:
                raise NotFound(f"Currency '{currency_id}' was not found in database.")

            currency_str = json.dumps(dict(row))
            return json.loads(currency_str)

        except Exception:
            logging.info("Close db connection.")
            close_db()
            raise

    @staticmethod
    def process_handler_delete_currency_by_id(currency_id):
        try:
            logging.info("Open db connection.")
            db = get_db()
            db.execute(queries.DEL_CURRENCY_BY_ID, (currency_id,))
            db.commit()

            logging.info("Close db connection.")
            close_db()

        except Exception:
            logging.info("Close db connection.")
            close_db()
            raise

    @staticmethod
    def process_handler_get_currencies():
        try:
            logging.info("Open db connection.")
            db = get_db()
            rows = db.execute(queries.CURRENCIES).fetchall()

            logging.info("Close db connection.")
            close_db()

            currencies_str = json.dumps([dict(x) for x in rows])
            currencies = json.loads(currencies_str)
            return dict(results=currencies)

        except Exception:
            logging.info("Close db connection.")
            close_db()
            raise

    def _payload_validations(self, payload):
        if not isinstance(payload, list):
            raise BadRequest("Payload type must be json format, not string.")

        req_validator = RequestValidator()

        for p in payload:
            # validate payload content
            req_validator.validate_payload(body=p)

            # verifying if currencyId (currency code) has a valid value
            req_validator.validate_currency_code(p['currencyId'])

            # validate unique field rules
            self._validate_unique_fields(p['currencyId'], p['currencyName'])

    @staticmethod
    def _validate_unique_fields(currency_id: str, currency_name: str):
        try:
            logging.info("Open db connection.")
            db = get_db()

            if db.execute(
                queries.CURRENCY_BY_ID, (currency_id,)
            ).fetchone() is not None:
                logging.info("Close db connection.")

                close_db()
                raise BadRequest(f"Already exist a currencyId '{currency_id}' registered.")

            if db.execute(
                queries.CURRENCY_BY_NAME, (currency_name,)
            ).fetchone() is not None:
                logging.info("Close db connection.")

                close_db()
                raise BadRequest(f"Already exist a currencyName '{currency_name}' registered.")

            logging.info("Close db connection.")
            close_db()

        except Exception:
            logging.info("Close db connection.")
            close_db()
            raise

    @staticmethod
    def _create_currencies(payload):
        try:
            logging.info("Open db connection.")
            db = get_db()
            for p in payload:
                db.execute(
                    queries.CREATE_CURRENCY, (
                        p['currencyId'], p['currencyName'],)
                )
                db.commit()

            logging.info("Close db connection.")
            close_db()

        except Exception:
            logging.info("Close db connection.")
            close_db()
            raise
