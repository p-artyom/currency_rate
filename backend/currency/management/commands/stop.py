from django.core.management.base import BaseCommand

from currency_rate.celery import app


class Command(BaseCommand):
    help = 'Удаление всех отложенных задач'

    def handle(self, *args, **options):
        try:
            app.control.purge()
            self.stdout.write(self.style.SUCCESS('Все задачи удалены!'))
        except Exception:
            self.stdout.write(self.style.ERROR('Ошибка при удалении задач!'))
