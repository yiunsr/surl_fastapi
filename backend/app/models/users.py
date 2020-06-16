from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func

from ..db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    created_dt = Column(DateTime(True), default=func.now(), nullable=False)
    updated_dt = Column(DateTime(True), default=func.now(),
                        onupdate=func.now(), nullable=False)

    is_active = Column(Boolean, default=True)
