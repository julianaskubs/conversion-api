# -*- coding: utf-8 -*-
from app import settings
import json
import requests

class ExternalReferenceAPI:

    def get(self, endpoint, querystr=None):
        return self.do_request(endpoint, querystr)

    def get_url(self, endpoint: str, querystr: str):
        self._host = settings.EXTERNAL_REF_API
        return f"https://{self._host}/api/v7/{endpoint}?{querystr}"

    def get_headers(self):
        return {
            'Accept': 'application/json'
        }

    def get_querystr(self, querystr):
        if isinstance(querystr, str):
            return f"{querystr}&compact=ultra&apiKey={settings.API_KEY}"
        else:
            return f"compact=ultra&apiKey={settings.API_KEY}"

    def do_request(self, endpoint, querystr, timeout=2):
        try:
            querystr = self.get_querystr(querystr)
            url = self.get_url(endpoint, querystr)
            headers = self.get_headers()

            response = requests.get(
                url,
                headers=headers,
                timeout=timeout,
                allow_redirects=False
            )
            return ExternalReferenceAPIResponse(response)

        except Exception as e:
            print(e)
            return None


class ExternalReferenceAPIResponse(object):
    def __init__(self, response):
        self._response = response

    def get_content(self):
        return self._response.json()

    def get_status(self):
        return self._response.status_code
