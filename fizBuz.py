for num in range(1, 51):
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If num is only divisible by 3, "Fizz" will be printed.
    elif num % 3 == 0:
        print("Fizz")
    # If num is only divisible by 5, "Buzz" will be printed.
    elif num % 5 == 0:
        print("Buzz")
    # num itself will be printed in all other cases.
    else:
        print(num)