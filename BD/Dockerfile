FROM postgres:14.8-alpine3.18

# Копируем файлы для инициализации базы данных
COPY ./initdb/ddl.sql /docker-entrypoint-initdb.d/ddl.sql
COPY ./database/movies.csv /docker-entrypoint-database.d/movies.csv

# (Необязательно) Копируем дополнительные скрипты
COPY ./src /scripts

# Устанавливаем Python и необходимые зависимости
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    gcc \
    musl-dev \
    postgresql-dev && \
    pip install --upgrade pip && \
    pip install pandas && \
    pip install psycopg2-binary && \
    pip install python-dotenv

# Запускаем Postgres и применяем dml.py
CMD ["sh", "-c", "docker-entrypoint.sh postgres & sleep 3 && python3 /scripts/dml.py && fg"]
