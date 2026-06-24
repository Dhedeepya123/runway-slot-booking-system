from pydantic import BaseModel


class BookingBase(BaseModel):
    flight_number: str
    airline: str
    runway: str
    date: str
    start_time: str
    end_time: str


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: int
    status: str

    class Config:
        from_attributes = True