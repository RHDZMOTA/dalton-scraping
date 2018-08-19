from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from model import *
import uuid


class Color(DataModel.base):
    __tablename__ = "color"
    id = Column("id", String, primary_key=True)
    model_id = Column("model_id", String)
    color = Column("color", String)
    src = Column("src", String)

    def __init__(self, model_id: str, color: str, src: str):
        self.id = str(uuid.uuid4())
        self.model_id = model_id
        self.color = color
        self.src = src
