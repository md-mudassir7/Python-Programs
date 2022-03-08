import random

def guess_number():
    for i in range(1,4):
        global guess
        guess = int(input('Guess the number between 1 and 20 : '))
        if guess > secret_number:
            print('Your number is too high')
        elif guess < secret_number:
            print('Your number is too low')
        else:
            break
    return guess


def check():
    if guess == secret_number:
        print('Conragulations you have guessed the number correctly')
    else:
        print('Better luck next time')
        print('The correct number was ' + str(secret_number))


secret_number=random.randint(1,20)
guess=guess_number()
check()
