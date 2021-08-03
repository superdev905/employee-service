import logging
from sqlalchemy.orm import Session
from ..modules.marital_status.model import MaritalStatus
from ..modules.nationality.model import Nationality
from ..modules.rsh.model import RSH
from ..modules.scholarship.model import Scholarship


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def seed_maritalStatus(db: Session):
    statusList = ["NO INFORMADO", "CASADO", "DIVORCIADO"	, "DIVORCIADO", "CONVIVIENTE"	, "SEPARADO"	,
                  "SEPARADO", "CONVIVIENTE"	, "SOLTERO"	, "SOLTERO CONVIVIENTE"	, "VIUDO", "FALLECIDO"]
    print("Seeding marital status")
    for item in statusList:
        found_status = db.query(MaritalStatus).filter(
            MaritalStatus.description == item).first()
        if not found_status:
            db_obj = MaritalStatus(description=item)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)


def seed_nationalities(db: Session):
    list = ["ARGENTINO", "BOLIVIANO", "CHILENO", "COLOMBIANO", "COSTARRICENSE", "CUBANO", "DOMINICANO", "ECUATORIANO", "GUATEMALTECO",
            "HONDUREÑO", "MEXICANO", "NICARAGÜENSE", "PANAMEÑO", "PARAGUAYO", "PERUANO", "PUERTORRIQUEÑO", "SALVADOREÑO", "URUGUAYO", "VENEZOLANO"]
    print("Seeding nationalities")
    for item in list:
        found_status = db.query(Nationality).filter(
            Nationality.description == item).first()
        if not found_status:
            db_obj = Nationality(description=item)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)


def seed_rsh(db: Session):
    list = [
        "EN PROCESO", "HASTA 40 %", "41 % A 50 %", "51 % A 60 %", "61 % A 70 %", "71 % A 80 %", "81 % A 90 %", "91 % A 100 %"
    ]
    print("Seeding nationalities")
    for item in list:
        found_status = db.query(RSH).filter(
            RSH.description == item).first()
        if not found_status:
            db_obj = RSH(description=item)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)


def seed_scholarship(db: Session):
    list = ["NO INFORMADO", "1° BÁSICO", "2° BÁSICO", "3° BÁSICO", "4° BÁSICO", "5° BÁSICO", "6° BÁSICO", "7° BÁSICO", "8° BÁSICO", "1° MEDIO", "2° MEDIO", "3° MEDIO", "4° MEDIO", "5° MEDIO",
            "ANALFABETO", "ESPECIAL", "KINDER", "LEE Y ESCRIBE", "PRE KINDER", "SALA CUNA", "TÉC/COM/IND COMPLETA", "TÉC/COM/IND INCOMPLETA", "UNIVERSITARIA COMPLETA", "UNIVERSITARIA INCOMPLETA"]
    for item in list:
        found_status = db.query(Scholarship).filter(
            Scholarship.description == item).first()
        if not found_status:
            db_obj = Scholarship(description=item)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
