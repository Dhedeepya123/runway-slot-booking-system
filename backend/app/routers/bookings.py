from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas, models
from ..database import get_db
from ..scheduler import has_conflict, find_next_available_slot

router = APIRouter(prefix="/bookings", tags=["Bookings"])


# CREATE BOOKING
@router.post("/")
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):

    all_bookings = crud.get_bookings(db)

    # Check conflict for SAME runway + same date
    for b in all_bookings:
        if b.runway == booking.runway and b.date == booking.date:
            if has_conflict(b.start_time, b.end_time,
                            booking.start_time, booking.end_time):

                # Suggest next available slot
                next_slot = find_next_available_slot(
                    all_bookings,
                    booking.start_time,
                    booking.end_time
                )

                return {
                    "message": "Conflict detected",
                    "suggested_slot": {
                        "start_time": next_slot[0],
                        "end_time": next_slot[1]
                    }
                }

    # No conflict → create booking
    return crud.create_booking(db, booking)


# GET ALL BOOKINGS
@router.get("/")
def get_all_bookings(db: Session = Depends(get_db)):
    return crud.get_bookings(db)


# GET SINGLE BOOKING
@router.get("/{booking_id}")
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.get_booking(db, booking_id)

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking


# APPROVE BOOKING
@router.put("/{booking_id}/approve")
def approve_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.update_status(db, booking_id, "Approved")

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking


# REJECT BOOKING
@router.put("/{booking_id}/reject")
def reject_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.update_status(db, booking_id, "Rejected")

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking


# DELETE BOOKING
@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.delete_booking(db, booking_id)

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {"message": "Deleted successfully"}