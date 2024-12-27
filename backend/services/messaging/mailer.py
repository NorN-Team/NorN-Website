from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="your_gmail@gmail.com",
    MAIL_PASSWORD="your_app_password",
    MAIL_FROM="your_gmail@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

async def send_email(email: str):
    message = MessageSchema(
        subject="Confirm your registration",
        recipients=[email],
        body="Welcome! Please confirm your email by clicking the link.",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    print(f" [x] Email sent to {email}")
