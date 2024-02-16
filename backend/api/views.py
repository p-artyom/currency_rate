from django.http import HttpRequest, HttpResponse
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CurrencySerializerInput, CurrencySerializerOutput
from currency.models import Currency


@extend_schema(
    summary='Получить курс валюты по отношению к рублю на заданную дату',
    description='Возвращает курс валюты по отношению к рублю на заданную дату',
    parameters=[
        OpenApiParameter(
            name='charcode',
            description='Код валюты',
            type=str,
            required=True,
        ),
        OpenApiParameter(
            name='date',
            description='Заданная дата',
            type=str,
            required=True,
        ),
    ],
    responses=CurrencySerializerOutput,
)
@api_view(['GET'])
def get_rate(request: HttpRequest) -> HttpResponse:
    '''Получить курс валюты по отношению к рублю на заданную дату.'''

    charcode = request.query_params.get('charcode')
    date = request.query_params.get('date')
    CurrencySerializerInput(
        data={'charcode': charcode, 'date': date},
    ).is_valid(raise_exception=True)
    currency = (
        Currency.objects.filter(
            charcode=charcode,
            created__date__lte=date,
        )
        .order_by('-created')
        .first()
    )
    if not currency:
        return Response(
            {'message': 'Данных нет!'},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = CurrencySerializerOutput(
        data={
            'charcode': currency.charcode,
            'date': currency.created.date(),
            'rate': currency.rate,
        },
    )
    serializer.is_valid(raise_exception=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
