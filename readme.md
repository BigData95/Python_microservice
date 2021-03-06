Implementation of two micro services with RabbitMq

## Requirements:

- Docker

- Docker Compose

- Free instance in cloudamqp or download RabbitMq and  change the consumers.py from each service.

## Usage

From root directory for admin and main run:

```bash
docker-compose up --build
```

Init Db's

In the Django app run

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

In the Flask app run

```bash
python3 manager.py db init
python3 manager.py db migrate
python3 manager.py db upgrade
```
## Endpoints

```
api/user      				[GET]
api/products				[GET, POST]
api/products/<id>			[GET, PUT, DELETE]
api/products/<id>/like		[POST]
```