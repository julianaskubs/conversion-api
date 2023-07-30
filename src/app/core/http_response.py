# -*- coding: utf-8 -*-
# import requests
from flask import jsonify


def ok_response():
    response = jsonify({'message': 'ok'})
    response.status_code = 200
    return response


def created_response():
    response = jsonify({'message': 'received'})
    response.status_code = 201
    return response


def server_error_response():
    response = jsonify({'message': 'An internal server error has occurred.'})
    response.status_code = 500
    return response


def bad_request_response(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response


def not_found_response(message):
    response = jsonify({'message': message})
    response.status_code = 404
    return response
