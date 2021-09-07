from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class HousingSituation(Base):
    __tablename__ = "housing_situation"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_id = Column(Integer,
                         ForeignKey('employee.id'), nullable=False)
    type_home_id = Column(Integer, nullable=False)
    property_home_id = Column(Integer, nullable=False)
    type_subsidy_id = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    state = Column(String(7), nullable=False, default="CREATED")
    is_main = Column(Boolean, nullable=False, default=True)
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    employee = relationship(
        "Employee",  uselist=False, lazy="select")
