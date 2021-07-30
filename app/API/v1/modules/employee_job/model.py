from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Float
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class EmployeeJob(Base):
    __tablename__ = "employee_job"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_id = Column(Integer,
                         ForeignKey('employee.id'), nullable=False)
    admission_date = Column(DateTime, nullable=False)
    business_id = Column(Integer, nullable=False)
    construction_id = Column(Integer, nullable=False)
    contract_term = Column(String(50), nullable=False)
    contract_type = Column(String(50), nullable=False)
    leave_date = Column(DateTime)
    leave_motive = Column(String(120))
    salary = Column(Float, nullable=False)
    state = Column(String(7), nullable=False, default="CREATED")
    created_by = Column(String(20), default="Jhon Doe")
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    employee = relationship(
        "Employee", back_populates="jobs", foreign_keys=[employee_id], lazy="select")
