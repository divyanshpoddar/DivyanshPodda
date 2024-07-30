from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional


def create_alert(db: Session, alert: schemas.AlertCreate, user_id: int):
    db_alert = models.Alert(**alert.dict(), owner_id=user_id)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert


def delete_alert(db: Session, alert_id: int):
    db_alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if db_alert:
        db.delete(db_alert)
        db.commit()
    return db_alert


def get_alerts(db: Session, user_id: int, status: Optional[str] = None):
    query = db.query(models.Alert).filter(models.Alert.user_id == user_id)
    if status:
        query = query.filter(models.Alert.status == status)
    alerts = query.all()
    return {"alerts": alerts, "total": len(alerts)}
