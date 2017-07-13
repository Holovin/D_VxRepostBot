from peewee import *
from storage.storage import Storage


class BaseModel(Model):
    class Meta:
        database = Storage.get()

