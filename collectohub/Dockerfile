# Используем официальный образ Python
FROM python:3.10-slim


# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код проекта в контейнер
COPY . .

# Выполняем миграции и собираем статику
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Открываем порт 8000
EXPOSE 8000

# Запускаем Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
