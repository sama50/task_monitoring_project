cd rabbitmq_celery_project
python manage.py runserver   

docker compose up

celery -A rabbitmq_celery_project  worker -l info -P gevent
celery -A rabbitmq_celery_project flower