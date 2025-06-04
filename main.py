from fastapi import FastAPI, HTTPException, Query
from models import FitnessClass, BookingRequest, Booking
from utils import load_json, save_json, convert_to_timezone
from datetime import datetime
from pytz import timezone

import os

app = FastAPI()

CLASSES_FILE = "data/classes.json"
BOOKINGS_FILE = "data/bookings.json"

@app.get("/classes")
def get_classes(timezone: str = "UTC"):
    classes = load_json(CLASSES_FILE)
    for cls in classes:
        cls['date_time'] = convert_to_timezone(cls['date_time'], timezone)
    return classes

@app.post("/book")
def book_class(booking: BookingRequest):
    classes = load_json(CLASSES_FILE)
    bookings = load_json(BOOKINGS_FILE)

    # Find the class
    cls = next((c for c in classes if c["id"] == booking.class_id), None)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")

    if cls["available_slots"] <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    # Decrease slot and save
    cls["available_slots"] -= 1
    save_json(CLASSES_FILE, classes)

    new_booking = {
        "class_id": booking.class_id,
        "client_name": booking.client_name,
        "client_email": booking.client_email,
        "booking_time": datetime.utcnow().isoformat()
    }
    bookings.append(new_booking)
    save_json(BOOKINGS_FILE, bookings)

    return {"message": "Booking successful", "booking": new_booking}

@app.get("/bookings")
def get_bookings(email: str = Query(..., description="Client email")):
    bookings = load_json(BOOKINGS_FILE)
    user_bookings = [b for b in bookings if b["client_email"] == email]
    return user_bookings