from django.db import models

from core.models import TimestampedModel
from currency.validators import CHARCODE_CHOICES


class Currency(TimestampedModel):
    charcode = models.CharField(
        'код валюты',
        max_length=3,
        choices=CHARCODE_CHOICES,
    )
    rate = models.DecimalField('значение', max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'

    def __str__(self) -> str:
        return self.charcode
