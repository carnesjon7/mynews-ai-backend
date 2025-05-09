# Hermes.Notifications: Email and SMS utility
import os
import smtplib
from email.message import EmailMessage

def send_email_notification(subject, body):
    sender = os.getenv("EMAIL_SENDER")
    recipient = os.getenv("CEO_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not recipient or not password:
        print("Missing email configuration.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Email notification sent.")
    except Exception as e:
        print(f"Email error: {e}")

def send_sms_notification(message):
    phone_number = os.getenv("CEO_PHONE")
    # SMS integration stub - would use Twilio or similar
    print(f"[SMS to {phone_number}]: {message}")
