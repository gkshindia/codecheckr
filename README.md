# Microservices with Docker, Flask, and React

Certain Commands to Remember

$ docker-compose -f docker-compose.yml up -d --build

$ docker-compose -f docker-compose.yml exec users python manage.py recreate_db

$ docker-compose -f docker-compose.yml exec users python manage.py seed_db

$ docker-compose -f docker-compose.yml exec users python manage.py test