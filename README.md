# **Skystore**

## **Описание**:

Skystore - интернет-магазин плагинов и утилит.


## **Установка**:

1. Клонируйте репозиторий

```
git@github.com:Alexandra-Chigrina/homework_22.git
```

2. В терминале инициализируйте Poetry и активируйте виртуальное окружение

```
poetry init
poetry shell
```
Или, если используете venv:
```commandline
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
3. Создайте .env на основе .env.example



## **Использование**:

### Запустите сервер и откройте сайт в браузере:.
```
python manage.py runserver
```

`http://127.0.0.1:8000/`

### Загрузка тестовых данных
```
python manage.py load_test_products
```
Загрузка фикстур вручную:
```
python manage.py loaddata catalog/fixtures/categories.json
python manage.py loaddata catalog/fixtures/products.json
```

### Создание суперпользователя
```
python manage.py createsuperuser
```
Панель администратора:
`http://127.0.0.1:8000/admin/`


### Описание основных модулей и функций

* catalog/views.py

Модуль содержит контроллеры для отображения страниц сайта:

`home(request)` — отображает главную страницу интернет-магазина (home.html) с описанием сервиса и витриной товара.

`contacts(request)` — обрабатывает страницу контактов (contacts.html):

- при GET-запросе отображает форму обратной связи.
- при POST-запросе извлекает данные формы (name, phone, message), выводит их в консоль и возвращает благодарственное сообщение.

`product_detail(request, pk)` — отображает страницу с подробной информацией о конкретном товаре.

`add_product(request)` — позволяет пользователю добавить новый товар через HTML-форму:

- при GET-запросе отображает форму добавления товара.
- при POST-запросе обрабатывает отправку формы:
  получает поля name, description, image, category, price;
  сохраняет новый товар в базу данных.

* catalog/models.py

Модуль, где описываются модели базы данных, то есть основные сущности проекта и их структура.

`Product` — наименование, описание, изображение, категория, цена, дата создания и обновления

`Category` — наименование и описание категории продукта

Используются ImageField, ForeignKey, Meta, __str__


## **Структура проекта**

├── catalog/                         # Основное приложение магазина
│   ├── migrations/                  # Миграции базы данных Django
│   ├── templates/                   # Шаблоны HTML
│       ├── catalog/                 # Шаблоны, относящиеся к приложению catalog
│           ├── includes/            # Подшаблоны (например, меню)
│               ├── inc_menu/        # Шаблон навигационного меню
│           ├── contacts.html        # Шаблон главной страницы
│           ├── home.html            # Шаблон страницы контактов с формой
│           ├── base.html            # Базовый шаблон для всех страниц 
│           ├── product_detail.html  # Шаблон страницы одного товара
│           ├── add_product.html     # Форма добавления нового товара 
│   ├── urls.py                      # Маршруты для catalog (home, contacts)
│   ├── admin.py                     # Настройка админки Django
│   ├── views.py                     # Контроллеры отображения страниц и обработки форм
│   ├── models.py                    # Модели Product и Category
│   ├── management/commands/         # Кастомные команды (load_test_products)
│   ├── templatetags                 # Пользовательские шаблонные теги
│       ├── my_tags.py               # Кастомные фильтры шаблонов (например, media_filter)
├── config/                          # Конфигурация проекта Django
│   ├── settings.py                  # Основные настройки проекта
│   ├── urls.py                      # Маршруты для всего проекта
├── media/catalog/                   # Медиафайлы, загруженные пользователями
│   ├── images.py                    # Папка для изображений товаров
├── static/                          # Статические файлы (CSS, JS, изображения)
│   ├── css/                         #
│       ├── bootstrap.min.css        # Bootstrap стилизация для шаблонов
│   ├── js/                          # 
│       ├── bootstrap.bundle.min.js  # Bootstrap функциональность                   # 
├── manage.py                        # Управляющий файл Django-проекта
├── .venv                            # Виртуальное окружение
├── .gitignore                       # Исключения файлов из Git
├── .flake8                          # Настройки линтера Flake8
├── .poetry.lock                     # Фиксированные зависимости проекта  
├── .pyproject.toml                  # Основной конфигурационный файл проекта  
├── .env                             # Переменные окружения (не загружается в Git) 
├── .env .sample                     # Шаблон .env
├── README.md                        # Документация  
