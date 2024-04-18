Crowdfunding-platform

Этот проект разработан с использованием фреймворка Django

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone 
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd django_project
    ```

3. Создайте и активируйте виртуальное окружение (опционально, но рекомендуется):

    ```bash
    python -m venv env
    source env/bin/activate
    ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Примените миграции:

    ```bash
    python manage.py migrate
    ```

## Запуск

Чтобы запустить сервер разработки Django, выполните следующую команду:

```bash
python manage.py runserver
