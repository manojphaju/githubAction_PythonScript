import os

def main():
    print('Hello from python script ')
    token = os.environ.get('MY_SECRET_TOKEN')
    if not token:
        RuntimeError('token not found')
    print('YEAH! all good. Token found.')


if __name__ == '__main__':
    main()