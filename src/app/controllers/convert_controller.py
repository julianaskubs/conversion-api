# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

bp = Blueprint('convert', __name__, url_prefix='/api')

class ConvertController:

    @bp.route('/convert', methods=['GET', 'POST'])
    def convert_controller():
        if request.method == "GET":
            return jsonify({"result":"ok"})
