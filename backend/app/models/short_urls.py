from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey

from ..db.base_class import Base


class ShortUrls(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String)
    org_url = Column(String)
    created_dt = Column(DateTime(True), default=func.now(), nullable=False)
    updated_dt = Column(DateTime(True), default=func.now(),
                        onupdate=func.now(), nullable=False)
    owner_user = Column(Integer, ForeignKey('User.id'))
    is_active = Column(Boolean, default=True)
