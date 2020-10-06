
''' YouTube Derrick Sherrill https://www.youtube.com/watch?v=byHi41L9vTM '''

###   INSERTION SORTING   ###

def insertion_sort(a_list):
    # start with all the values after the first sorted item hence range starts at 1
    indexing_length = range(1, len(a_list))

    # for all values in the indexing_length (unsorted list)
    for i in indexing_length:
        # get the value to be sorted
        value_to_sort = a_list[i]

        # while the left value(a_list[i-1]) is greater than ->
        # the right value(value_to_sort) AND greater than 0 ->
        # (python does negative indexing)
        while a_list[i-1] > value_to_sort and i > 0:
            # do the switch
            a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
            # compare down the list
            i = i - 1
    
    return a_list

print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))