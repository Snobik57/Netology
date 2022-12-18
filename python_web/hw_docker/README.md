## Task 1

Вы можете:

* загрузить docker-контейнер [отсюда](https://hub.docker.com/repository/docker/snobik57/netology-nginx)
* и запустить:
```bash
docker run -d -p 7777:80 snobik57/netology-nginx
```

Или:

* забрать файлы из репозитория GitHub
* создать образ:
```bash
docker build . -t snobik57/netology-nginx
```
* запустить образ:
```bash
docker run -d -p 7777:80 snobik57/netology-nginx
```

## Task 2

Вы можете:

* загрузить docker-контейнер [отсюда](https://hub.docker.com/repository/docker/snobik57/netology-django-crud)
* и запустить:
```bash
docker run -d -p 7777:6777 snobik57/netology-django-crud
```

Или:

* забрать файлы из репозитория GitHub
* создать образ:
```bash
docker build . -t snobik57/netology-django-crud
```
* запустить образ:
```bash
docker run -d -p 7777:6777 snobik57/netology-django-crud
```