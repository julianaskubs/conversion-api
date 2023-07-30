# -*- coding: utf-8 -*-
from app.core.external_api import CurrConvAPI

curr_conv_api = CurrConvAPI()


class ReferenceService:
    @staticmethod
    def process_handler():
        return curr_conv_api.get(endpoint='countries')
