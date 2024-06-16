from typing import Optional

from pydantic import BaseModel


class FormSchema(BaseModel):
    id: Optional[str] = None
    first_name: str
    last_name: str
    email: str
    country: str
    phone_number: str
    skills: list[str]
    experience: str
    compensation: str
    linkedin_url: Optional[str] = None
    timestamp: Optional[int] = None
