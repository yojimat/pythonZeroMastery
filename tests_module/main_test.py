import random


def do_stuff(num=0):
    try:
        if isinstance(num, int):
            return int(num) + 5
        else:
            return "Please enter a number"
    except ValueError as err:
        return err


def get_guess(number = None):
    try:
        return number or int(input("Guess a number 1~10:  "))
    except ValueError as e:
        print("Please enter a number")
        return e


def try_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("You are a genius!")
            return True
    else:
        print("Hey bozo, I said 1~10")
        return False


def guess_number():
    answer = random.randint(1, 5)

    while True:
        guess = get_guess()

        if isinstance(guess, ValueError):
            continue

        right_number = try_guess(guess, answer)

        if right_number:
            break

#guess_number()
