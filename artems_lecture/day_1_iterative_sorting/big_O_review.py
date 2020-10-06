''' Atrem's Lecture CSPT8 '''

####  BIG O NOTAION AND RUNTIMES REVIEW  ####

# Constant time O(1)
def print_num(n):
    print(n)

# Constant time O(1) even through it is running 10k times technically it's O(10k)
def print_num_10k(n):
    for num in range(10000):
        print(n)



# Linear time
def print_num_n_times(n): # O(n)
    for num in range(n):
        print(n) # O(1)


# adding the two functions together
def print_num_nested_times(n): # O(n * 10k)
    for num in range(n): # loop runs O(n) times
        print(n) # O(1)
        for num in range(10000): # O(10k)
            print(n)





animals = ['duck', 'jackal', 'hippo',
            'aardvark', 'cat', 'flamingo',
            'iguana', 'giraffe', 'elephant', 
            'bear', 'dog',
            ]
# Polynomial time
# double for loop
# prints out the possible pairs for each animal
def print_animal_pairs(): # O(n * n) = O(n^2)
    for animal_1 in animals: # O(n)
        for animal_2 in animals: # O(n)
            print(f'{animal_1} and {animal_2}') # O(1)


# Logarithmic Time
# input get reduced by a factor each iteration
def free_animals(animals):
    while len(animals) > 0:
        # take out half of the animals
        animals = animals[0: len(animals // 2)]
