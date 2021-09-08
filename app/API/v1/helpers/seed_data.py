from typing import List

from sqlalchemy.orm.session import Session


def seed_data(db: Session, items: List[str], model, property: str = "description"):

    for item in items:
        if property == "description":
            found_obj = db.query(model).filter(
                model.description == item.upper()).first()
            if not found_obj:
                obj_db = model(description=item.upper(), created_by=1)
                db.add(obj_db)
                db.commit()
                db.refresh(obj_db)
        else:
            found_obj = db.query(model).filter(
                model.name == item.upper()).first()
            if not found_obj:
                obj_db = model(name=item.upper(), created_by=1)
                db.add(obj_db)
                db.commit()
                db.refresh(obj_db)
