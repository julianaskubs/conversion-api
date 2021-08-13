# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

bp = Blueprint('token', __name__, url_prefix='/api')

# TODO route to get jwt for API authentication