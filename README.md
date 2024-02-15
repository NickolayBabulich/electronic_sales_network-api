# Electronic sales network

Торговая сеть электроники

## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DRF-FF5733?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![API](https://img.shields.io/badge/-API-4CAF50?style=flat)](https://en.wikipedia.org/wiki/Application_programming_interface)
[![Swagger](https://img.shields.io/badge/-Swagger-85EA2D?style=flat&logo=swagger&logoColor=white)](https://swagger.io/)
[![OOP](https://img.shields.io/badge/-OOP-FF5733?style=flat)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

## Описание:

Приложение платформы для торговой сети электроники. Представляет из себя управляемую БД с возможностью ведения учета
торговой сети, поставщиков электроники и продукции. Управление осуществляется авторизованным пользователем по средствам
админ-панели Django, а также с помощью API-интерфейсов.

Реализованно:

- модели БД
- вывод в админ-панель
- ссылка на поставщика в торговой сети
- фильтрация по городу
- custom действие очищающее задолженности в объекте торговой сети
- CRUD через API для моделей торговой сети и поставщик
- настроены права доступа для API-эндпоинтов
- добавлена документация описывающая API

## Настройка:

- Для начала работы с проектом клонируйте репозиторий:
    - ```git clone https://github.com/NickolayBabulich/participants_api.git```
- Отредактируйте файл .env.sample указав ваши данные, все заполненные данные в файле
  приведены для
  примера.
- После редактирования файла .env.sample переименуйте файл в .env
- установите зависимости ```pip install -r requirements.txt```

## Запуск:

- Подготовьте миграции БД командой ```python manage.py makemigrations```
- Подтвердите миграции БД командой ```python manage.py migrate```
- _Дополнительно:_ (не обязательный шаг) для удобства подготовлены тестовые данные для работы, установить их можно
  командой ```python manage.py loaddata esl_data.json```
- Создайте суперпользователя для управления командой ```python manage.py csu```
- **Запустите проект командой ```python manage.py runserver```**
- В случае успешного запуска перейдите в админ-панель ```/admin/``` для дальнейшей авторизации и управления

## Дополнительно

- API-эндпоинты проекта описаны по следующему пути ```/swagger/```
