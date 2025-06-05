# 🧘 Fitness Booking App (Backend API)

This is a backend system for booking fitness classes, built with **Flask**, **SQLAlchemy**, and **Flask-Migrate**. It supports creating classes,viewing classes, booking slots, and viewing bookings.

---

## 🚀 Setup Instructions

### 1. Clone the repo

git clone <repo-url>
cd fitness_booking_app

### 2. Create virtual environment

python -m venv venv

source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Initialize the database

flask db init

flask db migrate -m "Initial migration"

flask db upgrade

### 5. Run the server

python run.py

Server will start at: `http://127.0.0.1:5000`

## 📬 API Endpoints

### ✅ Create a Fitness Class
- **POST** `/classes/create`
- **Payload:**
{
  "name": "Yoga",
  "date_time": "2025-06-05 17:00:00",
  "instructor": "Suresh",
  "available_slots": 12
}

### 📅 Get All Classes
- **GET** `/classes`
- **Query Param:** `timeZone`
- **Example:**
  
curl "http://127.0.0.1:5000/classes?timeZone=Asia/Kolkata"

### 📝 Book a Class
- **POST** `/book`
- **Payload:**
{
  "class_id": "2db15078-5d51-4e09-a968-25da50cd19a6",
  "client_name": "Preeth",
  "client_email": "preeth@gmail.com"
}

### 📄 Get Bookings by Email
- **GET** `/bookings`
- **Query Param:** `email`
- **Example:**
  
curl "http://127.0.0.1:5000/bookings?email=preeth@gmail.com"

## 🗂️ Project Structure

fitness_booking_app/
│
├── run.py            # App entry point
├── config.py         # App config
├── requirements.txt  # Dependencies
├── migrations/       # DB migration files
├── app/
│   ├── __init__.py       # App factory
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API routes
│   ├── services/         # Business logic
│   └── utils/            # DB and logger setup
└── app.log           # Log file

## ✅ Tech Stack

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- CORS

---

## 📝 Logs

All activity is logged in `app.log`.
