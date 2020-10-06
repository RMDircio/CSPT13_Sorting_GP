import random
import time

my_range = 1000
my_size = 100

# list of sorted numbers
nums = list(range(0, my_size))

# same list from above but randomized(shuffled up)
shuffled_nums = list(range(0, my_size))
random.shuffle(shuffled_nums)

# # look at the list of numbers
# print(nums)
# print(shuffled_nums)

''' How to find certain number(s) in the list? '''

# number we are looking for
num_to_find = 12

# is a number in the list?
# Linear Time O(n)
def linear_search(arr, target): # arr == array or list and target = num_to_find
    ''' looks at a list and sees if a number is in the list '''
    for num in arr:
        if num == target:
            return True
    return False

# run the function
# print(linear_search(shuffled_nums, num_to_find))


''' Is there a way to approach this in a Binary Search Method? '''
# split the array in the middle and sort nodes accordingly


# new numbers
random_numbers = random.sample(range(my_range), my_size)

# # sort the new random numbers
random_numbers.sort()
print(random_numbers)



# speed clock for Linear Time
print("Linear Time")
start = time.time()
print(linear_search(random_numbers, num_to_find))
end = time.time()
print(f'Runtime: {end - start}')






# Numbers/arrays MUST BE STORTED - sorting is  NEVER linear
# make a function to select the middle number
def binary_search(arr, target): # arr == array or list and target = num_to_find
    # set up the array pointers
    start = 0
    end = (len(arr) - 1)

    found = False
    # if the end is greater/equal than the start
    while end >= start and not found :
        # find the middle index of the array - add the start and end and divide by 2
        middle_index = (start + end) // 2
        
        # compare the middle index with target
        # if the middle value == target, set found to be True
        if arr[middle_index] == target:
            found == True

        # change the 'end' of the array to be the 'middle' by length divided by 2(shrink the search space)
        else:
            # if middle value != target, is it smaller? - search the left side
            if target < arr[middle_index]:
                # move the `end` to the left
                end = middle_index - 1
            # if middle value != target, is it larger? - search the right side
            if target > arr[middle_index]:
                # move the `start` to the right
                start = middle_index + 1

    return found

# print(binary_search(random_numbers, 16))

# speed clock for Binary Time
print("Binary Time")
start = time.time()
print(binary_search(random_numbers, num_to_find))
end = time.time()
print(f'Runtime: {end - start}')
