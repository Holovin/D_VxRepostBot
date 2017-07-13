from peewee import *
from storage.base_model import BaseModel
from storage.userModel import User


class Sub(BaseModel):
    # db
    id = PrimaryKeyField(primary_key=True, null=False)

    # link
    user_id = ForeignKeyField(User, unique=True, null=False)

    # vk group id
    source_id = IntegerField(null=False)

    # last update for check with last post
    last_update = DateTimeField(null=False)

