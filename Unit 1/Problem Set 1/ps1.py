###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit = 10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips = []
    cowList = [] 
#    Returns a list that sorts the cow dict
    for i in sorted(cows, key = cows.get, reverse = False):
        cowList.append([i, cows[i]])
    
    cow = cowList.pop()
    currentTrip = [cow[0]]
    tripWeight = cow[1]
    while len(cowList) > 0:   
        for i in range(1, len(cowList) + 1):
            if tripWeight + cowList[-(i)][1] <= limit:
                currentTrip.append(cowList[-(i)][0])
                tripWeight += cowList[-(i)][1]

#       remove elements in cowList that we added to the current trip
        holderList = []
        for cow in cowList:
            if cow[0] not in currentTrip:
                holderList += [cow]
        cowList = holderList[:]
#        append current Trip to cow trip and make the new one the last element
#        in the sorted list.. Probably should have an if condition on fit
        trips.append(currentTrip)
        if len(cowList) > 1:
            cow = cowList.pop()
            currentTrip = [cow[0]]
            tripWeight = cow[1]
        elif len(cowList) == 1:
            trips.append([cowList.pop()[0]])
    return trips


        
            
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
#This is really bad....
    
    cowList = []
    for entry in cows:
        cowList.append(entry)
    for test in get_partitions(cowList):
        print(test)
#    Yup.. three for loops
    filteredList = []
    for cowGrouping in get_partitions(cowList):
        for cowGroup in cowGrouping:
            accepted = True
            totalWeight = 0
            for cow in cowGroup:
                totalWeight += cows[cow]
            if totalWeight > limit:
                accepted = False
                break
            totalWeight = 0
        if accepted:
            filteredList.append(cowGrouping)
            
    shortestListLen = 0
    shortestList = []
    for groups in filteredList:
        if (shortestListLen == 0 or len(groups) < shortestListLen):
            shortestListLen = len(groups)
            shortestList = groups
    return shortestList
            
#            
#    def groupWeights(partition, cowDict):
#        for group in partition:
    
    
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.asctime()
    greedy_cow_transport(cows,limit = 10)
    end = time.asctime()
    print("Start:", start + ", End:", end)
    start = time.asctime()
    brute_force_cow_transport(cows,limit=10)
    end = time.asctime()
    print("Start:", start + ", End:", end)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")

print(cows)
#limit = 100
#print(greedy_cow_transport(cows)) 
#print(brute_force_cow_transport(cows))

compare_cow_transport_algorithms()

