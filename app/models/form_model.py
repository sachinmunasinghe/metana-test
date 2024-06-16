import uuid
from datetime import datetime

from sqlalchemy import Column, String, JSON, Integer
from sqlalchemy.orm import Session

from ..database import Base


class FormModel(Base):
    __tablename__ = "forms"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    country = Column(String)
    phone_number = Column(String)
    skills = Column(JSON)
    experience = Column(String)
    compensation = Column(String)
    linkedin_url = Column(String)
    timestamp = Column(Integer, default=int(datetime.utcnow().timestamp()))

    @classmethod
    def get_form_by_id(cls, form_id: str, db: Session):
        return db.query(cls).filter(cls.id == form_id).first()

    @classmethod
    def get_forms(cls, db: Session):
        return db.query(cls).all()

    @classmethod
    def create_form(cls, form: 'FormModel', db: Session):
        db.add(form)
        db.commit()
        db.refresh(form)
        db.close()
        return form

    @classmethod
    def delete_form_by_id(cls, form: 'FormModel', db: Session):
        db.delete(form)
        db.commit()
