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