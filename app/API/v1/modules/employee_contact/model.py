from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class EmployeeContact(Base):
    __tablename__ = "employee_contact"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_run = Column(String(12), ForeignKey(
        'employee.run', ondelete="CASCADE"))
    address = Column(String(255), nullable=False)
    number = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    region_id = Column(Integer, nullable=False)
    commune_id = Column(Integer, nullable=False)
    housing_group = Column(String(255))
    block = Column(String(255))
    department = Column(String(255))
    mobile_phone = Column(String(9))
    landline_phone = Column(String(12))
    phone_owner = Column(String(200))
    other_phone = Column(String(9))
    email = Column(String(255), nullable=False, unique=True)
    is_confirmed = Column(Boolean, default=False)
    state = Column(String(7), nullable=False, default="CREATED")
    is_main = Column(Boolean, nullable=False, default=True)
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    employee = relationship(
        "Employee", back_populates="contacts", foreign_keys=[employee_run], lazy="select")
