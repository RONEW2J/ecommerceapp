# 🛒 Ecommerce Django Project
Этот проект — это простое e-commerce веб-приложение, разработанное на Django. В нем реализованы базовые функции для управления товарами, включая их создание, просмотр, обновление и удаление.

# 🚀 Функционал
📌 CRUD для продуктов (создание, просмотр, обновление, удаление)

🎨 Использование шаблонов Django (HTML-файлы в templates/store/)

🎯 Подключенные статические файлы (CSS-файл styles.css в static/css/)

# 📂 Структура проекта
store/ — основное приложение (модели, представления, маршруты)

migrations/ — файлы миграций базы данных

templates/store/ — шаблоны для отображения страниц

static/ — директория для статики (CSS, JS, изображения)

# ⚙ Установка и запуск
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Open a browser and go to http://localhost:8000/

# 🛠 Технологии
Django (Python 3.x)

HTML, CSS

SQLite (по умолчанию)
