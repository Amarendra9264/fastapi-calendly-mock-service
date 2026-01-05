from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta

from app.models.schema import AvailabilityRequest, BookingRequest
from app.data.bookings_store import BOOKED_SLOTS

router = APIRouter(tags=["Calendly Mock API"])


# --------------------------------------
# Appointment Types With Slot Duration
# --------------------------------------
APPOINTMENT_TYPES = {
    "consultation": 30,
    "follow_up": 15,
    "physio_session": 45
}


# --------------------------------------
# Slot Generator
# --------------------------------------
def generate_slots(start="09:00", end="17:00", duration=30):
    slots = []
    t = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")

    while t + timedelta(minutes=duration) <= end_time:
        slots.append(t.strftime("%H:%M"))
        t += timedelta(minutes=duration)

    return slots


# --------------------------------------
# Availability Endpoint
# --------------------------------------
@router.post("/availability")
def get_availability(req: AvailabilityRequest):

    if req.appointment_type not in APPOINTMENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid appointment type")

    # Validate date format
    try:
        datetime.strptime(req.date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(400, "Date must be YYYY-MM-DD")

    duration = APPOINTMENT_TYPES[req.appointment_type]

    all_slots = generate_slots(duration=duration)

    day_booked = BOOKED_SLOTS.get(req.date, [])

    available_slots = [
        slot for slot in all_slots if slot not in day_booked
    ]

    if not available_slots:
        return {
            "status": "no_availability",
            "date": req.date,
            "appointment_type": req.appointment_type,
            "available_slots": []
        }

    return {
        "status": "available",
        "date": req.date,
        "appointment_type": req.appointment_type,
        "slot_duration_minutes": duration,
        "available_slots": available_slots
    }


# --------------------------------------
# Booking Endpoint
# --------------------------------------
@router.post("/book")
def book_appointment(req: BookingRequest):

    if req.appointment_type not in APPOINTMENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid appointment type")

    if req.date not in BOOKED_SLOTS:
        BOOKED_SLOTS[req.date] = []

    if req.time in BOOKED_SLOTS[req.date]:
        raise HTTPException(status_code=409, detail="Slot already booked")

    BOOKED_SLOTS[req.date].append(req.time)

    booking_id = f"{req.date}-{req.time}-{req.patient_name.replace(' ', '').lower()}"

    return {
        "message": "Booking confirmed",
        "booking": {
            "booking_id": booking_id,
            "date": req.date,
            "time": req.time,
            "patient_name": req.patient_name,
            "appointment_type": req.appointment_type,
            "status": "confirmed"
        }
    }
