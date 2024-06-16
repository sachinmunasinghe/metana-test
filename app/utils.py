from sqlalchemy.orm import class_mapper


def model_to_dict(model):
    """
    Convert a SQLAlchemy model instance into a dictionary.

    :param model: SQLAlchemy model instance
    :return: dict representation of the model
    """
    return {c.key: getattr(model, c.key) for c in class_mapper(model.__class__).columns}
