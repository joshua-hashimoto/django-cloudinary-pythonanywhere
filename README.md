# django-cloudinary-anywhere

## docker-compose.yml

```yml
version: "3"

services:
    app:
        build: .
        command: gunicorn core.wsgi -b 0.0.0.0:8000
        env_file: ./.env
        volumes:
            - .:/app
        ports:
            - 8000:8000
        depends_on:
            - db
    db:
        image: mysql:5.7
        environment:
            MYSQL_DATABASE: django_cloudinary
            MYSQL_ROOT_PASSWORD: root
            MYSQL_USER: djc_user
            MYSQL_PASSWORD: djc_password
        ports:
            - 3306:3306
        volumes:
            - mysql_data:/var/lib/mysql

volumes:
    mysql_data:

```
