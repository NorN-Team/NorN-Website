# Устанавливаем базовый образ
FROM node:18 AS frontend

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY frontend/package.json frontend/package-lock.json ./

# Устанавливаем зависимости с флагом --legacy-peer-deps
RUN npm install --legacy-peer-deps

# Копируем исходный код
COPY frontend/ .

# Собираем проект
RUN npm run build

# Открываем порт
EXPOSE 3000

# Запускаем сервер
CMD ["npm", "start"]
