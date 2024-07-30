import redis
import smtplib
from email.mime.text import MIMEText
from app.config import settings
from app import crud, schemas
from app.database import SessionLocal

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

def check_alerts_and_notify(price: float):
    db = SessionLocal()
    alerts = crud.get_alerts(db, user_id=None)  # Adjust to get alerts for all users or use caching
    for alert in alerts['alerts']:
        if alert.coin_symbol == "BTCUSDT" and price >= alert.target_price:
            # Update alert status
            crud.update_alert_status(db, alert.id, "triggered")
            # Send email notification
            send_email(alert.owner_id, price)
    db.close()

def send_email(user_id: int, price: float):
    db = SessionLocal()
    user = crud.get_user(db, user_id=user_id)
    db.close()
    if user:
        msg = MIMEText(f"Price Alert Triggered! The price of BTC is now ${price}.")
        msg['Subject'] = "Price Alert Triggered"
        msg['From'] = settings.EMAIL_USER
        msg['To'] = user.email

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
            server.send_message(msg)
