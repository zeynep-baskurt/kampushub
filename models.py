from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Bir kulübün birden fazla etkinliği olabilir (1-to-N)
    events = relationship("Event", back_populates="club", cascade="all, delete-orphan")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False, index=True)
    description = Column(Text, nullable=True)
    location = Column(String(150), nullable=True)
    capacity = Column(Integer, nullable=False, default=100)  # Grup 4 (Registration) için kritik
    event_date = Column(DateTime, nullable=False)
    
    # Grup 5 (AI Service) tarafından doldurulacak alan
    category = Column(String(50), nullable=True, default="UNCATEGORIZED")

    # Bağlı olduğu kulüp (Foreign Key)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)

    # İlişki tanımı
    club = relationship("Club", back_populates="events")