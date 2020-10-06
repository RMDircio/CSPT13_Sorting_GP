'''   Artem's Lecture CSPT8   '''


'''
To see how this happens in real time - and any python code
http://www.pythontutor.com/live.html#mode=edit

Another YouTube visual example
https://www.youtube.com/watch?v=ROalU379l3U
'''


####    INSERTION SORTING    ###

# A way to 'manually' sort an array from smallest to biggest
# moving one value at a time over an imaginary line

def insertion_sort(list_to_sort): # at worst case this is O(n^2)
    # first element is already in the 'sorted side'

    # take action on all other items
    # starting at the second item, iterate until the end of the array
    for i in range(1, len(list_to_sort)):
        # the current number at the index represents value currently sorted
        current_num = list_to_sort[i]
        
        # move the current number back through the array (to the 'sorted side')
        j = i # make a new variable - this is the number that moves when we need to move backwards

        # keep moving until: its greater than the number before it OR we reach the start of the array
        while j > 0 and current_num < list_to_sort[j-1]:
            # shift/replace the current value and the one to the left of it (aka 'swap' them)
            list_to_sort[j] = list_to_sort[j-1]
            # decrement j as we go
            j -= 1

        # at this moment, j represents new location for the current number
        # set the value at the current index to the current number
        list_to_sort[j] = current_num

    return list_to_sort


# manual check
print(insertion_sort([8, 4, 2, 5, 1, 3]))