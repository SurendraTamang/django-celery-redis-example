# Django with Celery and Redis
It quick example how Django, Celery, Redis works together for learning purpose.



## Installation
- django
- redis
- python-dotenv
- celery


## Using Redis on Docker
```
docker run -p 6379:6379 --name local_redis redis
```

## Checking Celery 
```
celery -A inviteMe worker -l info
```

### Run
```
python manage.py runserver
```