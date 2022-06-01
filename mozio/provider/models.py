from django.db import models
from model_utils.models import TimeStampedModel

class Provider(TimeStampedModel):

    name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(null=False, blank=False, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=50)
    language = models.CharField(null=True, blank=True, max_length=50)
    currency = models.CharField(null=True, blank=True, max_length=50)


