def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item
 
    # returns returned, which now holds the value of fac_num's factorial
    return returned
 
 
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120