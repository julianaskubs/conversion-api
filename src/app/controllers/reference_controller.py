# -*- coding: utf-8 -*-
from app.core.services.reference_service import ReferenceService
from flask import Blueprint, request
from app.core.response import *

bp = Blueprint('reference', __name__, url_prefix='/api/references')

class ReferenceController:

    @bp.route('/', methods=['GET'])
    def get_references():
        '''
            Route to get references about countries and currencies
        '''
        response = ReferenceService().service_get_references()
        if not response:
            return server_error_response_msg()
        return response
