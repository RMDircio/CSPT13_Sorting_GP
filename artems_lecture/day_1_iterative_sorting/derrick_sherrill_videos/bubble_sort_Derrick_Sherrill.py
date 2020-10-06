''' YouTube Tutorial https://www.youtube.com/watch?v=g_xesqdQqvA '''

# Derrick Sherrill walkthrough

###   BUBBLE SORTING   ###

def bubble(a_list):
    # get the length that we are indexing (current list - 1)
    indexing_length = len(a_list) - 1
    
    # make a variable that will help break out of the while loop
    sorted = False

    # while the list is not sorted
    while not sorted: # when sorted is False
        sorted = True
        # for loop for comparison
        for i in range(0, indexing_length):
            # if the left item is greater than right item
            if a_list[i] > a_list[i+1]:
                # set the sort to false
                sorted = False
                # flip the two values in the list
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    
    return a_list # list is actually sorted now

print(bubble([4, 8, 6, 3, 2, 5, 7, 8, 9]))

# # code from description
# def bubble(list_a):
#     indexing_length = len(list_a) - 1 #SCan not apply comparision starting with last item of list (No item to right)
#     sorted = False #Create variable of sorted and set it equal to false

#     while not sorted:  #Repeat until sorted = True
#         sorted = True  # Break the while loop whenever we have gone through all the values

#         for i in range(0, indexing_length): # For every value in the list
#             if list_a[i] > list_a[i+1]: #"Angled brackets not allowed in Youtube Description :( list_a[i+1]: #if value in list is greater than value directly to the right of it,
#                 sorted = False # These values are unsorted
#                 list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
#     return list_a # Return our list "unsorted_list" which is not sorted.


# # print(bubble([4,8,1,14,8,2,9,5,7,6,6]))