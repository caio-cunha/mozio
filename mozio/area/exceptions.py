"""
File with custom exceptions 

Author: Caio Henrique Oliveira Cunha
Email: caiocomputacao2014@gmail.com
"""
from rest_framework.exceptions import APIException

class AreaNotFound(APIException):
    status_code = 422
    default_detail = {
        'code': 1422, 'msg': 'server - Area not found. Choose one ID that exist!'}
    default_code = 6001

class ProviderAreaNotFound(APIException):
    status_code = 422
    default_detail = {
        'code': 1422, 'msg': 'server - Not exist the provider ID choose!'}
    default_code = 6001