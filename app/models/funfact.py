from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.models import ModelBase


class FunFact(ModelBase):
    __tablename__ = "fun_fact"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(2500), nullable=False)

    def __str__(self):
        return self.title
