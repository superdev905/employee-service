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
    maternal_surname = Column(String(120), nullable=False)
    born_date = Column(DateTime, nullable=False)
    gender = Column(String(50), nullable=False)
    marital_status_id = Column(Integer, ForeignKey(
        'marital_status.id', ondelete='cascade'))
    scholarship_id = Column(Integer, ForeignKey(
        'scholarship.id', ondelete='cascade'))
    nationality_id = Column(Integer, ForeignKey(
        'nationality.id', ondelete='cascade'))
    job_id = Column(Integer, ForeignKey(
        'activity.id', ondelete='cascade'))
    relationship_id = Column(Integer, ForeignKey(
        'relationship.id', ondelete='cascade'))
    legal_charge = Column(String(2), nullable=False)
    rsh = Column(String(2))
    rsh_percentage_id = Column(
        Integer, ForeignKey('rsh.id', ondelete="cascade"))
    state = Column(String(7), nullable=False, default="CREATED")
    is_main = Column(Boolean, nullable=False, default=True)
    created_by = Column(String(20), default="Jhon Doe")
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    marital_status = relationship('MaritalStatus', uselist=False)
    scholarship = relationship('Scholarship', uselist=False)
    nationality = relationship('Nationality', uselist=False)
    job = relationship('Activity', uselist=False)
    relationship_detail = relationship('Relationship', uselist=False)
    rsh_percentage = relationship('RSH', uselist=False)
    employee = relationship(
        "Employee", back_populates="relatives", foreign_keys=[employee_run], lazy="joined")

