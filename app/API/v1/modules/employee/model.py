from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    run = Column(String(12), nullable=False, unique=True, primary_key=True)
    names = Column(String(120), nullable=False)
    paternal_surname = Column(String(120), nullable=False)
    maternal_surname = Column(String(120), nullable=True)
    born_date = Column(DateTime, nullable=False)
    gender = Column(String(50), nullable=False)
    marital_status_id = Column(Integer, nullable=False)
    scholarship_id = Column(Integer, nullable=False)
    disability = Column(String(2), nullable=False)
    credential_disability = Column(String(2), nullable=False)
    recognize = Column(String(2), nullable=False, default="NO")
    nationality_id = Column(Integer, nullable=False)
    alive = Column(String(2), nullable=False)
    bank_id = Column(Integer, nullable=False)
    account_type = Column(String(100))
    account_number = Column(String(100))
    rsh = Column(String(100))
    rsh_percentage = Column(String(100))
    rsh_status = Column(String(10))
    disability_type = Column(String(28))
    disability_percentage = Column(String(40))
    state = Column(String(7), nullable=False,
                   default="CREATED", server_default="CREATED")
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    contacts = relationship(
        "EmployeeContact", back_populates="employee", lazy="select")
    relatives = relationship(
        "EmployeeRelative", back_populates="employee", lazy="select")
    jobs = relationship(
        "EmployeeJob", back_populates="employee", lazy="select")
