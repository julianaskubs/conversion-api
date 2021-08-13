# -*- coding: utf-8 -*-
from flask import jsonify
from app.core.external_reference_api import ExternalReferenceAPI
from app.core.response import *

class ReferenceService:

    def service_get_references(self):
        try:
            endpoint = 'countries'
            api = ExternalReferenceAPI()
            response = api.get(endpoint)
            if response:
                return jsonify(response.get_content())

        except Exception as e:
            print(e)
            return server_error_response_msg()

