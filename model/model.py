from sqlalchemy import Column, String, ARRAY
from typing import List
from model import *


class Model(DataModel.base):
    __tablename__ = "model"
    id = Column("id", String, primary_key=True)
    name = Column("name", String)
    specs_pdf = Column("specs_pdf", String)
    interior = Column("interior", ARRAY(String))
    exterior = Column("exterior", ARRAY(String))

    def __init__(self, id: str, name: str, colors: List[Color], versions: List[Version], specs_pdf: str, interior: List[str], exterior: List[str]):
        self.id = id
        self.name = name
        self.colors = colors
        self.versions = versions
        self.specs_pdf = specs_pdf
        self.interior = interior
        self.exterior = exterior
