from itemsname import item_dnames, localnames, good
from matchdecode import hero


def main():
    print(item_dnames, localnames)
    guess = input()
    if str(guess) == str(hero[0]):
        print("U won", good[0])
    else:
        print("U lost ", good[0], hero[0],guess,type(hero[0]),type(guess))


if __name__ == '__main__':
    main()
