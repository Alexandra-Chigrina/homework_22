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


### Функциональность
Каталог
- Список товаров с пагинацией и кешированием.

- Детальная страница товара (кешируется на 15 минут).

- Добавление, редактирование и удаление товаров (CBV).

- Категории, изображения, цена, описание.

- Права доступа: только владелец или модератор может редактировать/удалять.

Контакты
- Форма обратной связи.

- Обработка POST-запросов и вывод в консоль.

Блог
- Статьи с публикацией, черновиками, превью и счётчиком просмотров.

- Email-уведомление при 100 просмотрах.

- Ограничение прав: только контент-менеджеры могут редактировать.

- Кеширование списка и детальной статьи.

Пользователи

- Регистрация пользователя с подтверждением email.

- Авторизация по email и паролю.

- Личный кабинет: редактирование профиля, аватар, телефон, страна.

- Приветственное письмо при регистрации.

- Права на редактирование своих товаров и статей.

Оптимизация и Redis

- Подключен Redis для кеширования.

- Низкоуровневое кеширование:

    * списка товаров;

    * списка товаров по категории;

    * детальной страницы товара.

- Переменная CACHE_ENABLED контролирует включение кеша.


### Основные контроллеры (CBV) 

catalog/views.py:

- ProductListView — отображает список товаров с пагинацией.

- ProductDetailView — подробности товара.

- ProductByCategoryView — список товаров в категории (с пагинацией и кешем).

- ProductCreateView — добавление нового товара.

- ProductUpdateView — редактирование товара.

- ProductDeleteView — удаление товара.

- ContactView — страница с формой обратной связи.

blog/views.py:

- BlogListView — список опубликованных статей.

- BlogDetailView — страница одной статьи с увеличением просмотров.

- BlogCreateView — добавление статьи.

- BlogUpdateView — редактирование статьи.

- BlogDeleteView — удаление статьи.

users/views.py:

- RegisterView — регистрация нового пользователя.

- LoginView, LogoutView — аутентификация.

- ProfileUpdateView — редактирование профиля пользователя.

- email_verification — подтверждение адреса email по токену.

## **Структура проекта**


├── blog/                                   # Основное приложение блога
│   ├── migrations/                         # Миграции базы данных Django
│   ├── templates/                          # Шаблоны HTML
│       ├── blog/                           # Шаблоны, относящиеся к приложению blog
│           ├── base.html        
│           ├── blog_confirm_delete.html        
│           ├── blog_detail.html        
│           ├── blog_form.html        
│           ├── blog_list.html        
│   ├── urls.py                             # Маршруты для blog
│   ├── admin.py                            # Настройка админки Django
│   ├── views.py                            # Контроллеры отображения страниц и обработки форм
│   ├── models.py                           # Модель Blog
│   ├── templatetags                        # Пользовательские шаблонные теги
│       ├── blog_tags.py                    # Кастомные фильтры шаблонов (например, media_filter)
├── catalog/                                # Основное приложение магазина
│   ├── migrations/                         # Миграции базы данных Django
│   ├── templates/                          # Шаблоны HTML
│       ├── catalog/                        # Шаблоны, относящиеся к приложению catalog
│           ├── includes/                   # Подшаблоны (например, меню)
│               ├── inc_menu/               # Шаблон навигационного меню
│           ├── base.html                   # Базовый шаблон для всех страниц 
│           ├── contacts.html         
│           ├── product_confirm_delete.html            
│           ├── product_detail.html            
│           ├── product_form.html            
│           ├── product_list.html            
│   ├── urls.py                             # Маршруты для catalog (home, contacts)
│   ├── admin.py                            # Настройка админки Django
│   ├── views.py                            # Контроллеры отображения страниц и обработки форм
│   ├── services.py                         # Бизнес-логика и кеширование
│   ├── models.py                           # Модели Product и Category
│   ├── forms.py                            # Кастомные формы
│   ├── management/commands/                # Кастомные команды (load_test_products)
│   ├── templatetags                        # Пользовательские шаблонные теги
│       ├── catalog_tags.py                 # Кастомные фильтры шаблонов (например, media_filter)
├── users/                                  # Приложение для управления пользователями
│   ├── templates/users/                    # Шаблоны регистрации, логина, профиля
│   ├── forms.py                            # Формы для регистрации и профиля
│   ├── models.py                           # Кастомная модель пользователя
│   ├── views.py                            # Представления для регистрации, логина, профиля
│   ├── urls.py                             # Маршруты users/ (register, login, logout, profile_edit)
├── config/                                 # Конфигурация проекта Django
│   ├── settings.py                         # Основные настройки проекта
│   ├── urls.py                             # Маршруты для всего проекта
├── media/                                  # Медиафайлы, загруженные пользователями
│   ├── catalog/images.py                   # Папка для изображений товаров
│   ├── blog/previews .py                   # Папка для превью постов
├── static/                                 # Статические файлы (CSS, JS, изображения)
│   ├── css/                         
│       ├── bootstrap.min.css               # Bootstrap стилизация для шаблонов
│   ├── js/                           
│       ├── bootstrap.bundle.min.js         # Bootstrap функциональность                   # 
├── manage.py                               # Управляющий файл Django-проекта
├── .venv                                   # Виртуальное окружение
├── .gitignore                              # Исключения файлов из Git
├── .flake8                                 # Настройки линтера Flake8
├── .poetry.lock                            # Фиксированные зависимости проекта  
├── .pyproject.toml                         # Основной конфигурационный файл проекта  
├── .env                                    # Переменные окружения (не загружается в Git) 
├── .env .sample                            # Шаблон .env
├── README.md                               # Документация  
