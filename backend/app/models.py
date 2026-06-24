from sqlalchemy import Column, Integer, String
from .database import Base


class RunwaySlot(Base):
    __tablename__ = "runway_slots"

    id = Column(Integer, primary_key=True, index=True)

    flight_number = Column(String, nullable=False)
    airline = Column(String, nullable=False)
    runway = Column(String, nullable=False)

    date = Column(String, nullable=False)

    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)

    status = Column(String, default="Pending")