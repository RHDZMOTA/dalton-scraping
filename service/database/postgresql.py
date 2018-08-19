from config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *


class Postgresql(object):

    def __init__(self):
        self.engine = create_engine(Settings.Database.connection_string)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        DataModel.base.metadata.create_all(self.engine)

    def add(self, obj):
        self.session.add(obj)

    def add_many(self, obj_list):
        for obj in obj_list:
            self.add(obj)

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()
