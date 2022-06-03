"""
Test Exceptions Endpoints Area

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from unittest.mock import patch
from truth.truth import AssertThat
from django.test import (
    TestCase,
    Client
)
import json
from provider.models import Provider
from area.models import Area
from rest_framework.permissions import IsAuthenticated

# -------------------------------------------
# Common
content_type_var = "application/json"

class AreaTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        # -------------------------------------------
        # Create one provider
        cls.provider = Provider.objects.create(
            name="Test Provider",
            email="test@mozio.com.br",
            phone="32120497",
            language="ENG",
            currency="BRL"
        )

        # -------------------------------------------
        # Create one provider
        cls.area = Area.objects.create(
            name="Test Area",
            price=205.0,
            geojson="[(0,0),(0,1),(1,1)]",
            provider_id=cls.provider.id
        )

    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_create_area(self, decode_user_from_token):
        """
        POST /apis/area:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/area"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": self.area.name,
            "price": self.area.price,
            "geojson": self.area.geojson,
            "provider": self.area.provider.id
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.post(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(401)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_create_area(self, decode_user_from_token):
        """
        POST /apis/area
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/area/"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

         # -------------------------------------------
        # Create the request body
        request_body = {
            "name": self.area.name,
            "price": self.area.price,
            "geojson": self.area.geojson,
            "provider": self.area.provider.id
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.post(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_validation_create_area(self, decode_user_from_token):
        """
        POST /apis/area
        400 Bad Request - Validation Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/area"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        request_body = {
            "price": self.area.price,
            "geojson": self.area.geojson
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.post(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(400)

    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_get_area(self, decode_user_from_token):
        """
        GET /apis/area:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/area"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(401)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_get_area(self, decode_user_from_token):
        """
        GET /apis/area:
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/areaas"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_patch_area(self, decode_user_from_token):
        """
        PATCH /apis/area:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/area"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": "New Name",
            "price": 1000,
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.patch(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(401)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_patch_area(self, decode_user_from_token):
        """
        PATCH /apis/area:
        404 Not Found ERROR  - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/areaas"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": "New Name",
            "price": 1000,
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.patch(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_delete_area(self, decode_user_from_token):
        """
        DELETE /apis/area:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/area"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.delete(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(401)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_delete_area(self, decode_user_from_token):
        """
        DELETE /apis/area:
        404 Not Found ERROR  - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/areaas"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area endpoint
        response = self.client.delete(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_filter_area_by_provider(self, decode_user_from_token):
        """
        GET /apis/area/filter/provider:
        422 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/area/filter/provider?provider_id={100000}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area/filter/provider?provider_id={} endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(422)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_filter_area_by_provider(self, decode_user_from_token):
        """
        GET /apis/area/filter/provider:
        422 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/area/filter/provider?provider_id={100000}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area/filter/provider?provider_id={} endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(422)

