# -*- coding: utf-8 -*-
import logging
from app import settings
import requests


class CurrConvAPI:
    def __init__(self):
        self.host = settings.API_DOMAIN

    def get_url(self, endpoint: str, query_str: str):
        url = f"https://{self.host}/api/v7/{endpoint}?{query_str}"
        logging.info(f"API URL for external request: {url}")
        return url

    @staticmethod
    def get_headers():
        return {
            'Accept': 'application/json'
        }

    @staticmethod
    def get_query_str(query_str):
        if isinstance(query_str, str):
            return f"{query_str}&compact=ultra&apiKey={settings.API_KEY}"
        else:
            return f"compact=ultra&apiKey={settings.API_KEY}"

    def do_request(self, endpoint, query_str, timeout=2):
        try:
            query_str = self.get_query_str(query_str)
            url = self.get_url(endpoint, query_str)
            headers = self.get_headers()

            logging.info("Starting request to external API")
            response = requests.get(
                url,
                headers=headers,
                timeout=timeout,
                allow_redirects=False
            )
            logging.info("Finished request to external API")
            return ExternalAPIResponse(response)

        except Exception:
            raise

    def get(self, endpoint=None, query_str=None):
        return self.do_request(endpoint, query_str)


class ExternalAPIResponse(object):
    def __init__(self, response):
        self.response = response

    def get_content(self):
        return self.response.json()

    def get_status(self):
        return self.response.status_code
