# schema/schema.py

from pydantic.dataclasses import dataclass
from typing import get_type_hints

@dataclass
class PersonSchema:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: str
    city: str
    state: str
    zip: str

def prompt_contact_input(schema_cls):
    fields = get_type_hints(schema_cls).keys()
    user_input = {field: input(f"{field.replace('_', ' ').title()}: ").strip() for field in fields}
    return schema_cls(**user_input)