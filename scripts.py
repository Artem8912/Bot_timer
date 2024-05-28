from random import randint
from time import sleep


def main():
    # Имитируем задержку
    sleep(3)
    print(f"Received items: {randint(0, 150)}")


if __name__ == '__main__':
    main()