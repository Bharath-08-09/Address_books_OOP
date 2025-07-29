# utils/validation.py

from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class PersonValidator(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    address: str
    city: str
    state: str
    zip: str

    @field_validator("phone_number")
    def valid_phone(cls, value):
        cleaned = value.replace(" ", "")
        if not cleaned.isdigit() or len(cleaned) < 10:
            raise ValueError("Invalid phone number format")
        return value

def validate_input(func):
    def wrapper(self, *args, **kwargs):  
        try:
            _ = PersonValidator(**kwargs)
        except ValidationError as e:
            raise ValueError(f"Invalid contact input: {e}")
        return func(self, *args, **kwargs)  
    return wrapper
