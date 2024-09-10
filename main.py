from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import date

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class BookingForm(BaseModel):
    first_name: str
    last_name: str
    email: str
    arrival_date: date
    departure_date: date
    country: str
    payment_mode: str

@app.get("/", response_class=HTMLResponse)
async def booking_form(request: Request):
    return templates.TemplateResponse("booking_form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_booking(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    arrival_date: date = Form(...),
    departure_date: date = Form(...),
    country: str = Form(...),
    payment_mode: str = Form(...)
):
    booking_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "arrival_date": arrival_date,
        "departure_date": departure_date,
        "country": country,
        "payment_mode": payment_mode
    }
    return templates.TemplateResponse("booking_success.html", {"request": request, "data": booking_data})

