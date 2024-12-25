# Backend Dockerfile
FROM python:3.11

WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY backend/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь backend-код
COPY backend/ .

EXPOSE 8000

CMD ["uvicorn", "movies:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
