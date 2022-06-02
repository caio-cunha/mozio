"""
Test Success Endpoints

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from truth.truth import AssertThat
from django.test import (
    TestCase,
    Client
)
import json
from rest_framework.permissions import IsAuthenticated
from unittest.mock import patch
from provider.models import Provider
from provider.serializers import ProviderSerializer

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

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_create_provider(self, decode_user_from_token):
        """
        POST /apis/provider:
        successfully create a provider
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/provider"

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
        AssertThat(response.status_code).IsEqualTo(201)

        # -------------------------------------------
        # Convert the response body back to dict
        response_data = json.loads(response.content)

        # -------------------------------------------
        # get last provider saved
        provider = Provider.objects.last()

        # -------------------------------------------
        # verify if last provider saved is igual the response of endpoint
        AssertThat(response_data).IsAnyOf(ProviderSerializer(provider).data)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_get_providers(self, decode_user_from_token):
        """
        GET /apis/provider:
        successfully list providers
        """

         # -------------------------------------------
        # Create the request url
        request_url = f"/apis/provider"

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
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Get all providers
        providers = Provider.objects.all()

        # -------------------------------------------
        # Evaluate if there is only one saved in database
        AssertThat(len(providers)).IsEqualTo(1)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_patch_providers(self, decode_user_from_token):
        """
        PATCH /apis/provider/{provider_id}:
        successfully update provider
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
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Convert the response body back to dict
        response_data = json.loads(response.content)

        # -------------------------------------------
        # Response data expected to return
        response_data_expected = {
            "id": self.provider.id,
             "name": "New Name",
            "email": "Newemail@test.com.br",
            "phone": self.provider.phone,
            "language": self.provider.language,
            "currency": self.provider.currency,
        }

        # -------------------------------------------
        # Evaluates whether the response data returned is the same as expected
        AssertThat(response_data).IsAnyOf(response_data_expected)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_delete_providers(self, decode_user_from_token):
        """
        DELETE /apis/provider/{provider_id}:
        successfully delete provider
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
        AssertThat(response.status_code).IsEqualTo(204)

        # -------------------------------------------
        # Evaluates if the provider was deleted
        deleted_provider = Provider.objects.all().filter(
            id=self.provider.id).first()

        AssertThat(deleted_provider).IsNone()

