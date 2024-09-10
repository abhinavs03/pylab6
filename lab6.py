import re
from datetime import datetime

def validate_travel_booking_form(name, passport_number, phone_number, email, departure_date, payment_method):
    if not re.match(r"^[A-Za-z\s]+$", name):
        return "Invalid name. Only alphabetic characters and spaces are allowed."
    
    if not re.match(r"^[A-Za-z0-9]{9}$", passport_number):
        return "Invalid passport number. It must be alphanumeric and exactly 9 characters long."
    
    if not re.match(r"^\d{10}$", phone_number):
        return "Invalid phone number. It must be a 10-digit number."
    
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return "Invalid email address format."
    
    try:
        datetime.strptime(departure_date, "%d/%m/%Y")
    except ValueError:
        return "Invalid departure date. Format must be 'dd/mm/yyyy'."
    
    if payment_method.lower() not in ['credit', 'debit', 'netbanking']:
        return "Invalid payment method. It must be either 'credit', 'debit', or 'netbanking'."
    
    return "All validations passed. Form is valid."

name = "Paul Walker"
passport_number = "A12345678"
phone_number = "9876543210"
email = "paul.walker@gmail.com"
departure_date = "25/12/2024"
payment_method = "credit"

validation_result = validate_travel_booking_form(name, passport_number, phone_number, email, departure_date, payment_method)
print(validation_result)


'''
All validations passed. Form is valid.
'''
