from sqlalchemy.orm import Session
from . import models, schemas


# Create booking
def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.RunwaySlot(
        flight_number=booking.flight_number,
        airline=booking.airline,
        runway=booking.runway,
        date=booking.date,
        start_time=booking.start_time,
        end_time=booking.end_time,
        status="Pending"
    )

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


# Get all bookings
def get_bookings(db: Session):
    return db.query(models.RunwaySlot).all()


# Get booking by ID
def get_booking(db: Session, booking_id: int):
    return db.query(models.RunwaySlot).filter(models.RunwaySlot.id == booking_id).first()


# Update status (Approve/Reject)
def update_status(db: Session, booking_id: int, status: str):
    booking = get_booking(db, booking_id)

    if booking:
        booking.status = status
        db.commit()
        db.refresh(booking)

    return booking


# Delete booking
def delete_booking(db: Session, booking_id: int):
    booking = get_booking(db, booking_id)

    if booking:
        db.delete(booking)
        db.commit()

    return booking