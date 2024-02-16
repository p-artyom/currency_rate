from rest_framework import serializers

from currency.models import Currency


class CurrencySerializerInput(serializers.ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = Currency
        fields = ('charcode', 'date')


class CurrencySerializerOutput(serializers.ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = Currency
        fields = ('charcode', 'date', 'rate')
