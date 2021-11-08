from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class EmployeeRelative(Base):
    __tablename__ = "employee_relative"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_run = Column(String(12),
                          ForeignKey('employee.run'), nullable=False)
    run = Column(String(12))
    names = Column(String(255), nullable=False)
    paternal_surname = Column(String(120), nullable=False)
    maternal_surname = Column(String(120))
    born_date = Column(DateTime, nullable=False)
    gender = Column(String(50), nullable=False)
    marital_status_id = Column(Integer, nullable=False)
    scholarship_id = Column(Integer,  nullable=False)
    nationality_id = Column(Integer, nullable=False)
    job_id = Column(Integer,  nullable=False)
    relationship_id = Column(Integer, nullable=False)
    legal_charge = Column(String(2), nullable=False)
    rsh = Column(String(2))
    rsh_percentage_id = Column(Integer)
    rsh_status = Column(String(10))
    phone = Column(String(9))
    state = Column(String(7), nullable=False, default="CREATED")
    is_main = Column(Boolean, nullable=False, default=True)
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    employee = relationship(
        "Employee", back_populates="relatives", foreign_keys=[employee_run], lazy="select")
