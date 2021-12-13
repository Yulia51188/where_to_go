# Куда пойти — Москва глазами Артёма

Cайт о самых интересных местах в Москве. Авторский проект Артёма. [Переходите на сайт](https://github.com/Yulia51188/where_to_go/edit/master/static/README.md) и смотрите, что интересного есть рядом с вами!

![](https://i.imgur.com/AOatQhR.jpg)

## Источники данных

Тестовые данные взяты с сайта [KudaGo](https://kudago.com). Готовые для загрузки данные можно найти по [ссылке](https://github.com/devmanorg/where-to-go-places).

## Что за проект?

Сайт "Куда пойти" содержит карту Москвы, на которой отмечены авторские любимые места с фотографиями и описанием. Кликните на маркер на карте и узнайте, что интересное есть прямо рядом с вами! Демо-версия сайта выложена на [pythonanywhere.com](https://www.pythonanywhere.com/) и доступна по [ссылке]().

## Хочу такой же

Исходный код доступен для скачивания в данном репозитории GitHub. Чтобы запустить сайт у себя на компьютере, понадобится:

- Скачайте код или воспольуйтесь git
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных `db.sqlite3` и сразу примените все миграции командой `python3 manage.py migrate`
- Создайте учетную запись администратора базы данных командой `python manage.py createsuperuser`
- Запустите сервер командой `python3 manage.py runserver`
- Доступ к сайту по адресу [127.0.0.1:8000](http://127.0.0.1:8000/), админка доступна по адресу [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

Через админку создавайте места с описанием, загружайте фотки и смотрите результаты на сайте! Для автоматизированной загрузки данных перейдите в раздел "Загрузка данных в базу".

![](https://i.imgur.com/Q4UBeLr.png)
![](https://i.imgur.com/KuL8LWx.png)

### Настройки

#TODO

### Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде
* [Django](https://www.djangoproject.com/start/) - серверная часть сайта, включая модель данных на Django ORM
* [environs](https://pypi.org/project/environs/) - загрузка переменных окружения
* [Pillow](https://pypi.org/project/Pillow/) - обработка изображений, используется для ImageField в моделях
* [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/en/latest/) - сортировка фотографий места
* [django-tinymce](https://github.com/jazzband/django-tinymce) - WYSIWYG-редактор HTML поля с подробным описанием места
* [dj-database-url](https://pypi.org/project/dj-database-url/) - парсинг URL базы данных

## Загрузка данных в базу

#TODO

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).



