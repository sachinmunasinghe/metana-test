from sqlalchemy.orm import Session

from app.models.form_model import FormModel
from app.schemas.form_schema import FormSchema
from app.utils import model_to_dict


class FormService:
    @classmethod
    def get_form_by_id(cls, form_id: str, db: Session):
        form_model = FormModel.get_form_by_id(form_id, db)
        if form_model is None:
            return None
        form_schema = FormSchema(**model_to_dict(form_model))
        return form_schema

    @classmethod
    def get_forms(cls, db: Session):
        form_model_list = FormModel.get_forms(db)
        form_schema_list = list(map(lambda x: FormSchema(**model_to_dict(x)), form_model_list))
        return form_schema_list

    @classmethod
    def create_form(cls, form_schema: FormSchema, db: Session):
        form_model = FormModel(**form_schema.model_dump())
        FormModel.create_form(form_model, db)
        form_schema = FormSchema(**model_to_dict(form_model))
        return form_schema

    @classmethod
    def delete_form_by_id(cls, form_id: str, db: Session):
        form_model = FormModel.get_form_by_id(form_id, db)
        if form_model is None:
            return None
        FormModel.delete_form_by_id(form_model, db)
        return 1
