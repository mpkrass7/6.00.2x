# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    print("First Element is:", first_elt)
    rest_list = some_list[1:]
    print("Rest of list is:", rest_list)
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        print("Appending", partial_subset, "to", subsets)
        subsets.append(partial_subset)
        print("Subsets now expanded to:", subsets)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
        print("Added first element to get:", subsets)
    print("Final subsets for loop:", subsets)
    return subsets

NUMBER = 3
def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False

get_all_subsets(test)