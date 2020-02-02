# Django tree test task #

Used python 3.7 + Django 3.0 + sqllite3.


Package for install ( _Ubuntu 18.x) _build-essential, python3.7-venv, python3.7-dev, python3-venv


1. Create virtualenv:
python3.7 -m venv .env```
2. Set virtualenv
``` . ./.env/bin/activate```
3. Install requirements:
```
pip install --upgrade pip
pip install -r requirements.txt
```
4. Execution of migrations:
```./manage.py migrate```
6. Fixtures DB fill (if necessary)
```./manage.py loaddata tree/fixtures/initial_data.json```
7. Run test :
```./manage.py test```
8. Установите pre-hook для запуска тестов
```cd .git/hooks```
```nano pre-commit```
```buildoutcfg
#!/bin/sh
. {path to env}/bin/activate
pytest --reuse-db
```
9. Запуск wsgi-сервера в фоне:
```gunicorn -c gunicorn.conf pena_backend.asgi```
или локально:
```./manage.py runserver 0.0.0.0:8000```
10. Запуск Celery:
```celery multi start 1 --pidfile=/root/celery.pid -A pena_backend
--logfile=/root/celery.log```
или локально:
```celery worker -A pena_backend -l debug```
11. Сервер доступен на 8000-м порту

http://penawash.com:8000/admin - админка
http://penawash.com:8000/docs - документация API

Аналогично на localhost.