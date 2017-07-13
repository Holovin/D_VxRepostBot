from dev.logger import logger_setup
from network.network import Network
from storage import userModel, subModel
from storage.storage import Storage


def main():
    logger_setup([Network.logger_name])
    Network()
    db = Storage.get()
    db.connect()
    db.create_tables([userModel.User, subModel.Sub])
    db.drop_tables([userModel.User, subModel.Sub])


if __name__ == '__main__':
    main()
