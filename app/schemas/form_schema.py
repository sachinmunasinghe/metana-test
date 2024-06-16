from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class FormSchema(BaseModel):
    id: Optional[str] = None
    first_name: constr(min_length=1, max_length=60)
    last_name: constr(min_length=1, max_length=60)
    email: EmailStr
    country: constr(min_length=1, max_length=60)
    phone_number: constr(pattern=r'^\d{10}$')
    skills: list[constr(min_length=1, max_length=30)]
    experience: constr(min_length=1, max_length=20)
    compensation: constr(min_length=1, max_length=30)
    linkedin_url: (
        Optional)[constr(min_length=1,
                         max_length=100,
                         pattern=r'^(https?://)?([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})(\.[a-zA-Z]{2,})?(/[^\s]*)?$')] = None
    timestamp: Optional[int] = None
