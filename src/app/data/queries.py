# -*- coding: utf-8 -*-

CURRENCY_BY_NAME = \
'SELECT * FROM currency WHERE currency_name = ?'

CURRENCY_BY_ID = \
'SELECT \
    currency_id as currencyId, \
    currency_name as currencyName \
FROM currency WHERE currency_id = ?'

CREATE_CURRENCY = \
'INSERT INTO currency (currency_id, currency_name) VALUES (?, ?)'

CURRENCIES = \
'SELECT \
    currency_id as currencyId, \
    currency_name as currencyName \
FROM currency'

DEL_CURRENCY_BY_ID = \
'DELETE FROM currency WHERE currency_id = ?'