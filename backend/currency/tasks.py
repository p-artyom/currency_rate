import logging

import requests

from currency.models import Currency
from currency_rate.celery import app

logger = logging.getLogger('main')


@app.task(bind=True)
def get_currency_rate(self) -> None:
    '''Получить актуальный курс валют.'''

    logger.info('Запущен процесс получения актуального курса валют!')
    sending_request.delay()


@app.task(bind=True)
def sending_request(self) -> None:
    '''Отправить запрос к сервису ЦБ.'''

    try:
        response = requests.get(
            'https://www.cbr-xml-daily.ru/daily_json.js',
        )
        if response.status_code == 200:
            logger.info('Данные получены!')
            create_records.delay(response.json()['Valute'])
        else:
            logger.error(f'Ошибка {response.status_code}!')
            logger.info('Повтор запроса данных через 5 минут!')
            return self.retry(countdown=300)
    except Exception:
        logger.error('Ошибка при отправлении запроса к сервису ЦБ!')
        logger.info('Повтор запроса данных через 5 минут!')
        return self.retry(countdown=300)


@app.task(bind=True)
def create_records(self, valute: dict) -> None:
    '''Создать записи в БД.'''

    for charcode in valute:
        Currency.objects.create(
            charcode=charcode,
            rate=valute[charcode].get('Value'),
        )
    logger.info('Данные созданы!')
    logger.info(
        'Повтор процесса получения актуального курса валют будет через сутки!',
    )
    get_currency_rate.apply_async(countdown=86400)
