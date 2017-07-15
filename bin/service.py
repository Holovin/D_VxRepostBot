import sys

from storage.userModel import User
from storage.subModel import Sub
from storage.storage import Storage


def main():
    db = Storage.get()
    db.connect()

    print('VxRepostBot service helper...')

    command = None

    if (len(sys.argv)) == 1:
        command = input('Enter command: ')

    else:
        command = sys.argv[1]

    print('Search [{}] command...'.format(command))

    # refresh db
    if command == 'db':
        db.create_tables([User, Sub], True)
        print('Renew tables ok')
        return

    # not found
    print('Command not found, service do nothing')

    db.disconnect()
    return

if __name__ == '__main__':
    main()
