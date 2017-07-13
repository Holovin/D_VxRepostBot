import sys


def main():
    print('VxRepostBot service helper...')

    command = None

    if (len(sys.argv)) == 1:
        command = input('Enter command: ')

    else:
        command = sys.argv[1]

    print('Search [{}] command...'.format(command))

    # do smthng
    if command == 'db_create':
        # TODO:
        return

    # not found
    print('Command not found, service do nothing')
    return

if __name__ == '__main__':
    main()
