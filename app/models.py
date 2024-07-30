from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)  # Specified length
    hashed_password = Column(String(255), nullable=False)  # Specified length

    alerts = relationship("Alert", back_populates="owner")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    coin_symbol = Column(String(50), nullable=False)  # Specified length
    target_price = Column(Float, nullable=False)
    status = Column(String(50), default="created", nullable=False)  # Specified length
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="alerts")
