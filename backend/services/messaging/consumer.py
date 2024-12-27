import pika
import json
import asyncio
from mailer import send_email

RABBITMQ_HOST = "rabbitmq"
QUEUE_NAME = "email_notifications"

def process_email(ch, method, properties, body):
    """
    Обработчик сообщений из очереди
    """
    message = json.loads(body)
    email = message.get("email")
    subject = message.get("subject")
    body_content = message.get("body")

    print(f"Получено сообщение: {message}")
    try:
        # Запускаем асинхронную задачу для отправки почты
        asyncio.get_event_loop().create_task(send_email(email))
        print(f" [x] Отправка email на {email}")
    except Exception as e:
        print(f"Ошибка при отправке email: {str(e)}")

    # Подтверждаем обработку сообщения
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Настройка подключения к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Прослушивание очереди
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=process_email)

print(f"Ожидание сообщений из очереди '{QUEUE_NAME}'. Для выхода нажмите CTRL+C")
channel.start_consuming()
