from dev.logger import logger_setup
from network.network import Network


def main():
    logger_setup([Network.logger_name])
    Network()


if __name__ == '__main__':
    main()
