
'''      Artem's Lecture CSPT8      https://www.youtube.com/watch?v=kpCa2PhWECs&feature=youtu.be '''


                 ####      RECURSIVE      ####

# print every number from N to zero
def print_numbers(n):


    # # iterative way
    # for i in range(n, 0, 1): # (start, end, #of steps)
    #     print(i)
    

    # recursive way - ALWAYS needs a base case -code to break out of loop
    # RUNTIME is the runtime for each line TIMES the number of times the function is called
    # This example is O(n)

    
    # base case
    if n == 0: # if n is 0 then break out
        return
    
    # recursive case
    print_numbers(n-1)



# SECOND EXAMPLE

def double_print_num(n):
    print(n)
    if n == 0:
        return
    
    double_print_num(n - 1)
    double_print_num(n - 1)
    return



###   ANOTHER EXAMPLE OF RECURSION   ###

# Fibonacci Sequence

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# fib(n) = fib(n-1) +fib(n-2)

# base case
# at n = 0 --> fib(0) == 0
# at n = 1 --> fib(1) == 1

def fibonacci(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # recursive case
    result = fibonacci(n-1) +fibonacci(n-2)
    return result