# Куда пойти — Москва глазами Артёма

Cайт о самых интересных местах в Москве. Авторский проект Артёма. [Переходите на сайт](https://yuly6a.pythonanywhere.com/) и смотрите, что интересного есть рядом с вами!

![](https://i.imgur.com/AOatQhR.jpg)

## Источники данных

Тестовые данные взяты с сайта [KudaGo](https://kudago.com). Готовые для загрузки данные можно найти по [ссылке](https://github.com/devmanorg/where-to-go-places).

## Что за проект?

Сайт "Куда пойти" содержит карту Москвы, на которой отмечены авторские любимые места с фотографиями и описанием. Кликните на маркер на карте и узнайте, что интересное есть прямо рядом с вами! Демо-версия сайта выложена на [pythonanywhere.com](https://www.pythonanywhere.com/) и доступна по [ссылке](https://yuly6a.pythonanywhere.com/).

## Хочу такой же

Исходный код доступен для скачивания в данном репозитории GitHub. Чтобы запустить сайт у себя на компьютере, понадобится:

- Скачайте код или воспольуйтесь git
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных `db.sqlite3` и сразу примените все миграции командой `python3 manage.py migrate`
- Создайте учетную запись администратора базы данных командой `python manage.py createsuperuser`
- Запустите сервер командой `python3 manage.py runserver`
- Доступ к сайту по адресу [127.0.0.1:8000](http://127.0.0.1:8000/), админка доступна по адресу [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

Через админку создавайте места с описанием, загружайте фотки и смотрите результаты на сайте! Для автоматизированной загрузки данных перейдите в раздел "Загрузка данных в базу".

### Настройки

В проекте используются следующие переменные окружения:
- `DEBUG` - флаг отладочного режима Django, по умолчанию False
- `SECRET_KEY` - секретный ключ проекта Django
- `DATABASE_URL` - ссылка на базу данных для последующего парсинга с помощью [dj-database-url](https://pypi.org/project/dj-database-url/), по умолчанию создается файл `db.sqlite3`.

### Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) — для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде
* [Django](https://www.djangoproject.com/start/) — серверная часть сайта, включая модель данных на Django ORM
* [environs](https://pypi.org/project/environs/) v загрузка переменных окружения
* [Pillow](https://pypi.org/project/Pillow/) — обработка изображений, используется для ImageField в моделях
* [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/en/latest/) — сортировка фотографий места
* [django-tinymce](https://github.com/jazzband/django-tinymce) — WYSIWYG-редактор HTML поля с подробным описанием места
* [dj-database-url](https://pypi.org/project/dj-database-url/) — парсинг URL базы данных

## Загрузка данных в базу

### Создание объектов в админке

Вы можете создавать места вручную через админку сайта. Интерфейс позволяет загружать картинки, интерактивно менять их порядок и редактировать описание в удобном HTML редакторе.

![](https://i.imgur.com/Q4UBeLr.png)
![](https://i.imgur.com/KuL8LWx.png)

### Загрузка данных по ссылке на JSON файл

В терминале сервера или локальной машины введите команду `load_place`:
```bash
$ python manage.py load_place "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Места, где снимался  фильм «Операция „Ы“ и другие приключения Шурика».json" operaciya_i

```
Команда принимает обязательный аргумент - URL адрес JSON файла как в примере и необзятельный - слаг места, который по умолчанию задается равным 'place'.
Если данное место уже существует, то картинки по ссылкам полностью обновятся.

Пример файла:
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

### Загрузка данных из папки локальной машины

Воспользуйтесь командой `load_place` с флагом '-f' и в базу будут загружены места из всех файлов в указанной папке:

```bash
$ python manage.py load_place "/home/yulia/Dropbox/Devman Edu/Django/#1_Where_To_Go/where-to-go-places-master/places" -f
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).



