# Используем официальный образ Node.js
FROM node:20-alpine

# Устанавливаем рабочую директорию
WORKDIR /frontend

# Копируем файлы package.json и yarn.lock
COPY package.json yarn.lock ./

# Устанавливаем зависимости
RUN yarn install

# Копируем весь проект
COPY . .

# Указываем порт
EXPOSE 3000

# Запускаем React-приложение
CMD ["yarn", "start"]
