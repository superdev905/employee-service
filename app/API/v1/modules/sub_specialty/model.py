from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class SubSpecialty(Base):
    __tablename__ = "sub_specialty"
    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False, unique=True)
    parent_specialty_id = Column(Integer, ForeignKey(
        'specialty.id', ondelete="CASCADE"), nullable=False)
    created_by = Column(String(20), default="Jhon Doe")
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    update_at = Column(DateTime(timezone=True),
                       nullable=False,
                       onupdate=func.now(), server_default=func.now())
    parent_specialty = relationship(
        'Specialty', back_populates="sub_specialties", lazy="select")
