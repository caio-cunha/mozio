"""
Test Success Endpoints Area

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
from area.models import Area
from provider.models import Provider
from area.serializers import AreaSerializer

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
        cls.provider_02 = Provider.objects.create(
            name="Test Provider 02 ",
            email="test02@mozio.com.br",
            phone="3212049789",
            language="ENG",
            currency="BRL"
        )

        # -------------------------------------------
        # Create one area
        cls.area = Area.objects.create(
            name="Test Area",
            price=200.0,
            geojson="[(0,0),(0,2),(2,2)]",
            provider_id=cls.provider.id
        )

        # -------------------------------------------
        # Create one area
        cls.area_02 = Area.objects.create(
            name="Test Area 02",
            price=400.0,
            geojson="[(0,0),(0,0.3),(0.3,0.3)]",
            provider_id=cls.provider_02.id
        )

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_create_area(self, decode_user_from_token):
        """
        POST /apis/area:
        successfully create a area
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
            "name": "Test Area",
            "price": 200.0,
            "geojson": "[(0,0),(0,2),(2,2)]",
            "provider": self.provider.id
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
        # get last area saved
        area = Area.objects.last()

        # -------------------------------------------
        # verify if last provider saved is igual the response of endpoint
        AssertThat(response_data).IsAnyOf(AreaSerializer(area).data)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_get_area(self, decode_user_from_token):
        """
        GET /apis/area:
        successfully list area
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
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Get all areas
        areas = Area.objects.all()

        # -------------------------------------------
        # Evaluate if there is only one saved in database
        AssertThat(len(areas)).IsEqualTo(2)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_patch_areas(self, decode_user_from_token):
        """
        PATCH /apis/area/{area_id}:
        successfully update area
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/area/{self.area.id}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Create the request body
        request_body = {
            "name": "New Name",
            "price": 2000.0,
            "geojson": self.area.geojson
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
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Convert the response body back to dict
        response_data = json.loads(response.content)

        # -------------------------------------------
        # Response data expected to return
        response_data_expected = {
            "id": self.area.id,
            "name": "New Name",
            "price": 2000.0,
            "provider": self.provider.id,
            "geojson": self.area.geojson,
        }

        # -------------------------------------------
        # Evaluates whether the response data returned is the same as expected
        AssertThat(response_data).IsAnyOf(response_data_expected)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_delete_area(self, decode_user_from_token):
        """
        DELETE /apis/area/{area_id}:
        successfully delete area
        """

        # -------------------------------------------
        # Create the request url
        request_url = f"/apis/area/{self.area.id}"

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
        AssertThat(response.status_code).IsEqualTo(204)

        # -------------------------------------------
        # Evaluates if the area was deleted
        deleted_area = Area.objects.all().filter(
            id=self.area.id).first()

        AssertThat(deleted_area).IsNone()

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_filter_by_provider_get_area(self, decode_user_from_token):
        """
        GET /apis/area/filter/provider:
        successfully list area filtered by provider
        """

         # -------------------------------------------
        # Create the request url
        request_url = f"/apis/area/filter/provider?provider_id={self.provider.id}"

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
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Get all areas
        areas = Area.objects.filter(provider=self.provider.id)

        # -------------------------------------------
        # Evaluate if there is only one saved in database
        AssertThat(len(areas)).IsEqualTo(1)

    @patch.object(IsAuthenticated, 'has_permission', return_value = True)
    def test_successfully_filter_by_coordinates_get_area(self, decode_user_from_token):
        """
        GET /apis/area/filter/coordinate:
        successfully list area filtered by coordinate
        """

         # -------------------------------------------
        # Create the request url
        request_url = f"/apis/area/filter/coordinate?lat={0.5}&long={1}"

        # -------------------------------------------
        # Create the request header
        request_header = {
            "HTTP_AUTHORIZATION": "access_token"
        }

        # -------------------------------------------
        # Simulate a http call to the /apis/area/filter/coordinate?lat={}&long={} endpoint
        response = self.client.get(
            request_url,
            **request_header
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Get all areas
        areas = Area.objects.filter(id=self.area.id)

        # -------------------------------------------
        # Evaluate if there is only one saved in database
        AssertThat(len(areas)).IsEqualTo(1)