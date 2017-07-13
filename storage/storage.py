from peewee import SqliteDatabase


class Storage:
    storage = None

    @staticmethod
    def get():
        if Storage.storage is None:
            Storage.storage = SqliteDatabase('storage.db')

        return Storage.storage
