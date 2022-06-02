"""
Test Exceptions Endpoints

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

class ProviderTest(TestCase):

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
    def test_unauthorized_create_provider(self, decode_user_from_token):
        """
        POST /apis/provider:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/provider"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": self.provider.name,
            "email": self.provider.email,
            "phone": self.provider.phone,
            "language": self.provider.language,
            "currency": self.provider.currency,
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
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
    def test_not_found_create_provider(self, decode_user_from_token):
        """
        POST /apis/providers
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/providerss/"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

         # -------------------------------------------
        # Create the request body
        request_body = {
            "name": self.provider.name,
            "email": self.provider.email,
            "phone": self.provider.phone,
            "language": self.provider.language,
            "currency": self.provider.currency,
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/providers endpoint
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
    def test_not_found_validation_create_provider(self, decode_user_from_token):
        """
        POST /apis/providers
        404 Not Found ERROR - Validation Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/providers"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

         # -------------------------------------------
        # Create the request body
        request_body = {    
            "phone": self.provider.phone,
            "language": self.provider.language,
            "currency": self.provider.currency,
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/providers endpoint
        response = self.client.post(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_get_provider(self, decode_user_from_token):
        """
        GET /apis/provider:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/provider"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(401)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_get_provider(self, decode_user_from_token):
        """
        GET /apis/providers
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/providerss/"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/providers endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_patch_provider(self, decode_user_from_token):
        """
        PACTH /apis/provider:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/provider"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": "New Name",
            "email": "Newemail@test.com.br",
        }


        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
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
    def test_not_found_patch_provider(self, decode_user_from_token):
        """
        PATCH /apis/providers
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/providerss/"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

         # -------------------------------------------
        # Create the request body
        request_body = {
            "name": "New Name",
            "email": "Newemail@test.com.br",
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
        response = self.client.patch(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_patch_provider_id_url(self, decode_user_from_token):
        """
        PATCH /apis/providers
        422 Not Found ERROR - Provider ID not found Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/provider/100000"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": "New Name",
            "email": "Newemail@test.com.br",
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
        response = self.client.patch(
            request_url,
            content_type=content_type_var,
            data=json.dumps(request_body),
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(422)


    @patch.object(IsAuthenticated, 'has_permission', return_value = False)
    def test_unauthorized_delete_provider(self, decode_user_from_token):
        """
        DELETE /apis/provider:
        401 Unauthorized ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/provider/{self.provider.id}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
        response = self.client.delete(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(401)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_not_found_delete_provider(self, decode_user_from_token):
        """
        DELETE /apis/providers
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/providerss/{self.provider.id}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
        response = self.client.delete(
            request_url,
            **request_header
        )
        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_protect_error_delete_provider(self, decode_user_from_token):
        """
        DELETE /apis/providers
        422 Not Found ERROR - Protect Field Provider ID Exception Test
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/provider/{self.provider.id}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/provider endpoint
        response = self.client.delete(
            request_url,
            **request_header
        )
        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(422)