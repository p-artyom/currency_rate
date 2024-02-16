# Курс валют

## Описание

Реализовано _Django_-приложение, которое отображает курс валюты по отношению к
рублю на заданную дату. Для получения текущего курса валюты необходимо
отправить запрос к приложению по адресу `http://127.0.0.1:8000/api/rate/?`
`charcode=EUR&date=2024-02-16`. Написана команда, которая создаёт задачу на
обращение к сервису ЦБ за актуальными курсами валют. Задача повторяется раз в
сутки.

## Технологии

- Python 3.10.12;
- PostgreSQL 14;
- Django 4.2.5;
- Django REST framework 3.14.0;
- Gunicorn 21.2.0;
- Nginx 1.22.1;
- Celery 5.3.4;
- Redis 5.0.1.

## Запуск приложения локально в docker-контейнерах

Инструкция написана для компьютера с установленной _ОС Windows_ 10 или 11.

- Установите _Windows Subsystem for Linux_ по инструкции с официального сайта
[Microsoft](https://learn.microsoft.com/ru-ru/windows/wsl/install);

- Зайдите на
[официальный сайт Docker](https://www.docker.com/products/docker-desktop/),
скачайте и установите файл _Docker Desktop_;

- В корне двух микросервисов создайте .env файл и заполните следующими данными:

  - в переменной `POSTGRES_DB` должно быть название базы данных;

  - в переменной `POSTGRES_USER` должно быть имя пользователя БД;

  - в переменной `POSTGRES_PASSWORD` должен быть пароль пользователя БД;

  - в переменной `DB_HOST` должен быть адрес, по которому _Django_ будет
  соединяться с базой данных;

  - в переменной `DB_PORT` должен быть порт, по которому _Django_ будет
  обращаться к базе данных;

  - в переменную `SECRET_KEY` укажите секретный ключ для конкретной установки
  _Django_;

  - в переменную `DEBUG` укажите значение режима отладки;

  - в переменную `ALLOWED_HOSTS` укажите список строк, представляющих имена
  хоста/домена, которые может обслуживать это _Django_ приложение;

  - в переменные `CELERY_BROKER_URL` и `CELERY_RESULT_BACKEND` укажите _URL_-
  адреса, на которые будут отправляться сообщения и записываться результаты.

- В терминале в папке с `docker-compose.yml` выполните команду:

```text
docker compose up
```

- Перейдите в новом терминале в директорию, где лежит файл
`docker-compose.yml`, и выполните команду:

```text
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

- И далее выполните команду, которая создаст задачу на обращение к сервису ЦБ
за актуальными курсами валют. Задача будет раз в сутки повторяться:

```text
docker compose exec backend python manage.py start
```

- Команда, которая удалит все задачи из очереди:

```text
docker compose exec backend python manage.py stop
```

- На странице `http://127.0.0.1:8000/api/docs/` можно ознакомиться с
документацией проекта.

## Автор

[Пилипенко Артем](https://github.com/p-artyom)
