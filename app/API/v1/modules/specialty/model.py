from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import DateTime
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class Specialty(Base):
    __tablename__ = "specialty"
    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False, unique=True)
    created_by = Column(String(20), default="Jhon Doe")
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    sub_specialties = relationship(
        'SubSpecialty', back_populates="parent_specialty", lazy="select")
