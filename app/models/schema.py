from pydantic import BaseModel


class AvailabilityRequest(BaseModel):
    date: str
    appointment_type: str


class BookingRequest(BaseModel):
    date: str
    time: str
    patient_name: str
    appointment_type: str
