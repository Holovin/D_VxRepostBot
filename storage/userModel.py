from datetime import datetime
from peewee import *
from storage.base_model import BaseModel


class User(BaseModel):
    # db
    id = PrimaryKeyField(primary_key=True, null=False)

    # for stats
    reg_date = DateTimeField(default=datetime.now(), null=False)

    # user / admin
    role_id = IntegerField(default=0, null=False)

    # prevent spam for inactive users
    is_active = BooleanField(default=True, null=False)

    # telegram user id
    telegram_id = IntegerField(unique=True, null=False)

    # vk user id
    vk_id = IntegerField(default=None, unique=True, null=True)

