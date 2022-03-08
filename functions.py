import random

def rand_num(abc):
    if abc == 1:
        return 'The number is 1'
    if abc == 2:
        return 'The number is 2'
    if abc == 3:
        return 'The number is 3'
    if abc == 4:
        return 'The number is 4'
    if abc == 5:
        return 'The number is 5'

print(rand_num(random.randint(1,5)))
