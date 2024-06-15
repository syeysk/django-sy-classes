# Установка На Linux

Скачайте репозиторий:

```sh
git clone https://github.com/syeysk/django-sy-classes && cd django-sy-classes && git checkout dev
```

Заполните переменные окружения, добавив и заполнив файл `.env`

Соберите образ и запустите контейнер:

```sh
docker-compose -f docker-compose.yml up -d --build
```

## Проверка доступности сервера

<http://127.0.0.1:8006/>

## Настройте Nginx + Debian для глобального доступа

Создайте файл `/etc/nginx/conf.d/classes.intera.space` и запишите в него настройки для Nginx:

```
server {
    listen 80;
    listen [::]:80;
    server_name classes.intera.space www.classes.intera.space;
    root /usr/share/nginx/html/django-sy-classes;
    location / {
        proxy_pass http://127.0.0.1:8006;
    }
    location /static/ {
        sendfile on;
        root /usr/share/nginx/html/django-sy-classes;
    }
    location /media/ {
        sendfile on;
        root /usr/share/nginx/html/django-sy-classes/media;
    }
    location = /favicon.ico {
       sendfile on;
       root /usr/share/nginx/html/django-sy-classes/static;
    }
}
```

Если нужно установить сертификат SSL для домена, то [следуйте инструкциям](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/) - поправка: возможно, на Вашем сервере нужно вместо команды `python` использовать `python3`.
Если Вы ранее выполняли команды из этой инструкции для других серверов Платформы, то достаточно выполнить команду `sudo certbot --nginx -d classes.intera.space -d www.classes.intera.space`, чтобы получить сертификат.
