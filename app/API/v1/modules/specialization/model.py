from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class Specialization(Base):
    __tablename__ = "specialization"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_id = Column(Integer,
                         ForeignKey('employee.id'), nullable=False)
    specialty_id = Column(Integer, nullable=False)
    specialty_detail_id = Column(Integer, nullable=False)
    is_self_taught = Column(String(2), nullable=False)
    certifying_entity_id = Column(Integer)
    is_certificated = Column(String(2))
    certification_file_id = Column(Integer, ForeignKey("attachment.id"))
    certificated_date = Column(DateTime)
    state = Column(String(7), nullable=False, default="CREATED")
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    employee = relationship("Employee",  uselist=False, lazy="select")
    certification_file = relationship(
        "Attachment",  uselist=False, lazy="joined")
