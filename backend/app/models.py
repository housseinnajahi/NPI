from sqlalchemy import Column, Float, Integer, String

from .postgres import postgres


class Calculation(postgres.base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, nullable=False)
    result = Column(Float, nullable=False)
