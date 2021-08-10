# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

bp = Blueprint('token', __name__, url_prefix='/api')

class TokenController:

    @bp.route('/token', methods=['GET', 'POST'])
    def convert_controller():
        if request.method == "GET":
            return jsonify({"result":"ok"})

