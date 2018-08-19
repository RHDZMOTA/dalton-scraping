from sqlalchemy import Column, String, Float
from model import *

import re
import uuid


class Version(DataModel.base):
    __tablename__ = "version"
    id = Column("id", String, primary_key=True)
    model_id = Column("model_id", String)
    version = Column("version", String)
    price = Column("price", Float)
    description = Column("description", String)

    def __init__(self, model_id: str, html_description: str):
        self.id = str(uuid.uuid4())
        self.model_id = model_id
        self.html_description = html_description
        self.version = re.search('<h3>(.*)</h3>', html_description).group(1)
        self.price = float(re.search('">(.*)</h5>', html_description).group(1).replace("$", "").replace(",", ""))
        self.description = [desc.strip() for desc in re.search('<ul>([\s\S.]*)</ul>', html_description).group(1).strip().replace("<li>", " ").replace("</li>", ".").split("\n")]
