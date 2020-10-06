
''' YouTube Tutorial https://www.youtube.com/watch?v=DnvWAd-RGhk&t=12s '''

# Derrick Sherrill walkthrough

###   BINARY SORTING   ###


# list needs to be sorted before doing binary search
def binary_search(sequence, item):
    # set a start and end
    begin_index = 0
    end_index = len(sequence) -1  # python has negative indices

    # while the start is less than or equal to the end
    while begin_index <= end_index:
        # set the middle value
        # middle value = start + remaining list items, then divide w/o a remainder floor division ( // 2 )
        midpoint = begin_index + (end_index - begin_index) // 2

        # compare the midpoint value (not the index) to target
        midpoint_value = sequence[midpoint]

        # if middle value is equal to target
        if midpoint_value == item:
            # return the middle index
            return midpoint
        
        # if target is less ( to the left ) than middle value
        elif item < midpoint_value:
            # set the end index to the middle index - 1
            end_index = midpoint - 1

        # otherwise
        else:
            # set the start to middle index +1 - check only the items to the right
            begin_index = midpoint + 1

    # when while loop breaks if target is NOT in list
    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 12

# print the index of the item_a
# will return None is item_a is not in list
print(binary_search(sequence_a, item_a))