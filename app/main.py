from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database, auth
from app.database import engine
from app.auth import get_current_user
from app.websocket_listener import start_price_tracking

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/alerts/create/", response_model=schemas.Alert)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.create_alert(db=db, alert=alert, user_id=current_user.id)

@app.delete("/alerts/delete/{alert_id}", response_model=schemas.Alert)
def delete_alert(alert_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db_alert = crud.get_alert(db=db, alert_id=alert_id, user_id=current_user.id)
    if db_alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return crud.delete_alert(db=db, alert_id=alert_id)

@app.get("/alerts/", response_model=schemas.AlertList)
def get_alerts(status: str = None, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.get_alerts(db=db, user_id=current_user.id, status=status)

if __name__ == "__main__":
    import uvicorn
    start_price_tracking()
    uvicorn.run(app, host="0.0.0.0", port=8000)
