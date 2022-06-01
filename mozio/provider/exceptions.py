"""
File with custom exceptions 

Author: Caio Henrique Oliveira Cunha
Email: caiocomputacao2014@gmail.com
"""
from rest_framework.exceptions import APIException

class ProviderNotFound(APIException):
    status_code = 422
    default_detail = {
        'code': 1422, 'msg': 'server - Provider not found. Choose one ID that exist!'}
    default_code = 6001