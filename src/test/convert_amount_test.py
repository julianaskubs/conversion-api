# -*- coding: utf-8 -*-
from app.core.services.convert_service import ConvertService

cs = ConvertService()

def test_product_value_conversion_usd():
    mock_rate = 0.190511
    brl_amount = '50'  # R$ 0,50 to USD
    amount1 = cs.convert(brl_amount, mock_rate)
    brl_amount = '100'  # R$ 1,00 to USD
    amount2 = cs.convert(brl_amount, mock_rate)
    brl_amount = '52929'  # R$ 529,29 to USD
    amount3 = cs.convert(brl_amount, mock_rate)
    assert amount1 == 0.10
    assert amount2 == 0.19
    assert amount3 == 100.84


def test_product_value_conversion_eur():
    mock_rate = 0.161497
    brl_amount = '50'  # R$ 0,50 to EUR
    amount1 = cs.convert(brl_amount, mock_rate)
    brl_amount = '100'  # R$ 1,00 to EUR
    amount2 = cs.convert(brl_amount, mock_rate)
    brl_amount = '52929'  # R$ 529,29 to EUR
    amount3 = cs.convert(brl_amount, mock_rate)
    assert amount1 == 0.08
    assert amount2 == 0.16
    assert amount3 == 85.48


def test_product_value_conversion_ars():
    mock_rate = 18.496468
    brl_amount = '50'  # R$ 0,50 to ARS
    amount1 = cs.convert(brl_amount, mock_rate)
    brl_amount = '100'  # R$ 1,00 to ARS
    amount2 = cs.convert(brl_amount, mock_rate)
    brl_amount = '52929'  # R$ 529,29 to ARS
    amount3 = cs.convert(brl_amount, mock_rate)
    assert amount1 == 9.25
    assert amount2 == 18.50
    assert amount3 == 9790.00


def test_product_value_conversion_inr():
    mock_rate = 14.139187
    brl_amount = '50'  # R$ 0,50 to INR
    amount1 = cs.convert(brl_amount, mock_rate)
    brl_amount = '100'  # R$ 1,00 to INR
    amount2 = cs.convert(brl_amount, mock_rate)
    brl_amount = '52929'  # R$ 529,29 to INR
    amount3 = cs.convert(brl_amount, mock_rate)
    assert amount1 == 7.07
    assert amount2 == 14.14
    assert amount3 == 7483.73