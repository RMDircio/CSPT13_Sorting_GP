
'''      Artem's Lecture CSPT8      '''

# Introduction to Divide and Conquer

''' 
Quick Sort:
Use divide and Conquer to break problem down into smaller steps.
1. Choose a pivot - normally first number in list
2. Move all elements less than pivot to the left of pivot
3. Move all elements greater than pivot to the right of pivot
4. Repeat steps 2-3 on left and right

'''

import time

# function to break up numbers into left, pivot and right
def partition(numbers): # O(n)
    # divide - how to properly split our data
    left = []
    pivot = numbers[0]
    right = []

    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]: # start the loop at the 1 index
        if num <= pivot: # if value is  less/equal to pivot
            left.append(num) # append number to the left
        
        else:
            right.append(num) # append number to the right



    return left, pivot, right



# example of quick sort

def quicksort(numbers): # O(log(n)
    # base case - easiest array to sort?
    if len(numbers) <= 1:
        return numbers
    
    # divide
    left, pivot, right = partition(numbers) # O(n)
    # make sure pivot is array with size 1
    pivot = [pivot] # sorted

    # make whole array sorted
    sorted_array = quicksort(left) + pivot + quicksort(right) # O(n)
    return sorted_array


# manual check
print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))
    
