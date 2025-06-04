# 🏋️‍♂️ Fitness Studio Booking API

A simple FastAPI-based backend for managing bookings in a fictional fitness studio. Clients can view classes and book available slots.

---

## 🚀 Features

- View all upcoming classes with timezone conversion
- Book a class with email validation
- Retrieve all bookings by email
- Stores data in flat JSON files (no database)
- Built with FastAPI and Pydantic

---

## 📁 Project Structure

fitness_booking_api/
├── main.py # FastAPI endpoints
├── models.py # Pydantic models
├── utils.py # Timezone & file helpers
├── data/
│ ├── classes.json # Seed fitness classes
│ └── bookings.json # Stores bookings
├── requirements.txt # Dependencies
└── README.md # This file


---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone  https://github.com/patt2303/fitness_booking_api.git
cd fitness_booking_api
python -m venv .venv
.venv\Scripts\activate       # For Windows
source .venv/bin/activate    # For macOS/Linux
pip install -r requirements.txt
python -m uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs for Swagger UI.

