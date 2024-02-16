from django.core.management.base import BaseCommand

from currency.tasks import get_currency_rate


class Command(BaseCommand):
    help = 'Создать задачу на получение актуального курса валют'

    def handle(self, *args, **options):
        try:
            get_currency_rate.delay()
            self.stdout.write(self.style.SUCCESS('Задача создана!'))
        except Exception:
            self.stdout.write(self.style.ERROR('Ошибка при создании задачи!'))
