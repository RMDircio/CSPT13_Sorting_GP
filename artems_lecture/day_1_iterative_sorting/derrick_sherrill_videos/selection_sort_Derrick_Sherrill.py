
''' YouTube Derrick Sherrill https://www.youtube.com/watch?v=4CykZVqBuCw'''

###   SELECTION SORTING   ###
##   A mix of insertion and bubble sorting   ##

def selection_sort(a_list):
    # get the range of what we need to compare
    indexing_length = range(0, len(a_list) - 1)
    
    # for every element in the unsorted list
    for i in indexing_length:
        # set the first element in the unsorted list as default min value
        min_value = i

        # for every element to the right of i
        for j in range(i + 1, len(a_list)):
            # if element is less than current min value
            if a_list[j] < a_list[min_value]:
                # replace the min value
                min_value = j
        
        # if the min value is lower than the default
        if min_value != i:
            # switch the items
            a_list[min_value], a_list[i] = a_list[i], a_list[min_value]

    return a_list


print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))