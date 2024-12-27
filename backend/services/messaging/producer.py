import pika
import json

# Конфигурация RabbitMQ
RABBITMQ_HOST = "rabbitmq" 
EXCHANGE_NAME = "email_exchange"
QUEUE_NAME = "email_notifications"
ROUTING_KEY = "email.key"

# Установка соединения с RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Создание обменника и очереди
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="direct", durable=True)
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

def send_registration_email(email: str):
    """
    Отправить email через RabbitMQ
    """
    message = {"email": email, "subject": "Подтверждение регистрации", "body": "Спасибо за регистрацию!"}
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=ROUTING_KEY,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)  # Устанавливаем сообщения как "persistent"
    )
    print(f"Сообщение отправлено в RabbitMQ: {message}")
