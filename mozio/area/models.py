from django.db import models
from model_utils.models import TimeStampedModel
from provider.models import Provider

class Area(TimeStampedModel):

    name = models.CharField(null=False, blank=False, max_length=100)
    price = models.FloatField(null=False, blank=False)
    provider = models.ForeignKey(Provider, null=False, blank=False, on_delete=models.PROTECT)
    geojson = models.JSONField()

    
