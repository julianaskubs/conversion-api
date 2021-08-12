# -*- coding: utf-8 -*-
from flask import jsonify

def create_response_msg(message, status):
    response = jsonify({ 'message': message })
    response.status_code = status
    return response

def server_error_response_msg():
    response = jsonify({ 'message': 'An internal server error has occurred.' })
    response.status_code = 500
    return response