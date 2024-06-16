import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas.form_schema import FormSchema
from ..services.form import FormService

router = APIRouter(
    prefix="/forms",
    tags=["forms"],
)


@router.get("/", response_model=list[FormSchema])
async def get_forms(db: Session = Depends(get_db)):
    try:
        return FormService.get_forms(db)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=500, detail='Internal server error')


@router.post("/", response_model=FormSchema)
async def create_form(form: FormSchema, db: Session = Depends(get_db)):
    try:
        return FormService.create_form(form, db)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=500, detail='Internal server error')


@router.get("/{form_id}", response_model=FormSchema)
async def get_form(form_id: str, db: Session = Depends(get_db)):
    try:
        response = FormService.get_form_by_id(form_id, db)
        if response is None:
            raise HTTPException(status_code=404, detail="Form not found")
        return response
    except Exception as e:
        if type(e) is not HTTPException:
            logging.exception(e)
            raise HTTPException(status_code=500, detail='Internal server error')
        raise e


@router.delete("/{form_id}", response_model=None)
async def delete_form(form_id: str, db: Session = Depends(get_db)):
    try:
        if FormService.delete_form_by_id(form_id, db) is None:
            raise HTTPException(status_code=404, detail="Form not found")
    except Exception as e:
        if type(e) is not HTTPException:
            logging.exception(e)
            raise HTTPException(status_code=500, detail='Internal server error')
        raise e
