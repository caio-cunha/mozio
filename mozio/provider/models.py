from django.db import models
from model_utils.models import TimeStampedModel

LANGUAGE_CHOICES = [
    ('BRA', 'Brazil'),
    ('SPA', 'Spanish'),
    ('ENG', 'English'),
    ('CHI', 'Chinese'),
]

CURRENCY_CHOICES = [
    ('BRL', 'Real'),
    ('EUR', 'Euro'),
    ('JPY', 'Japanese Yen'),
    ('USD', 'US Dollar'),
]

class Provider(TimeStampedModel):

    name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(null=False, blank=False, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=50)
    language = models.CharField(null=True, blank=True, max_length=3, choices=LANGUAGE_CHOICES)
    currency = models.CharField(null=True, blank=True, max_length=3, choices=CURRENCY_CHOICES)


