'''
This is exercise 2 for Assignment 2 ENSF 338
'''

import json
import sys
import timeit

sys.setrecursionlimit(20000) # set the maximum recursion depth to 20000, as default is 1000

def func1(arr, low, high): 
    '''
    
    Arguments: 

    arr (array) = array with all integer values
    low (integer) = index in array, should be the smallest number in arr
    high (integer) = index in array, that should be the highest value in arr
    '''
    if low < high: 
        # 1 OPERATION
        pi = func2(arr, low, high) # calls for the second function 
        func1(arr, low, pi-1) # pi is the high position, and minus one as current position is already sorted
        func1(arr, pi + 1, high)


def func2(array, start, end):
    '''
    
    Arguments: 
    array (integer array) = the same integer array as in func1
    start (intger) = index value in array, smaller than end
    end (integer) = index value in array, bigger than start
    '''
    # We are going to optimize this function choosing a better pivot value rather than the start of the array block
    # if there are items in this this block of array with more than 2 elements
    # mid = start + ( (end - start) // 2)
    # make a new array with only the first, last and the middle element 
    # sort those elements in that array from smallest to largest
    # as there are only 3 elements, the median value between them would be the second item
    # else:
        # there only 2 elements between them 
        # let p equal the first value in that array

    if (end - start >= 2):
        mid = start + ((end -start) // 2)
        pivots = [array[start], array[mid],array[end]]
        pivots.sort()
        p = pivots[1]

    else:
        p = array[start] 
    
    low = start + 1
    
    high = end 
   
    while True: 

        while low <= high and array[high] >= p: 
            
            high = high - 1 
            
        while low <= high and array[low] <= p: 
            low = low + 1 
        
        if low <= high:
            array[low], array[high] = array[high], array[low]
  
        else:
            break

    array[start], array[high] = array[high], array[start] 

    return high


filename = "/Users/owner/Documents/YEAR2/W23_Y2/ENSF338/Assignment2/ex2.json"
times =[]

with open(filename, "r") as file:
    data = json.load(file)
    #data has 10 arrays 
    i = 0 
    for items in data:
        executed_time = timeit.timeit(lambda:func1(data[i], 0, (len(data[i]) - 1)) , number =1)
        times.append(executed_time)
        i = i + 1
    
print("Timing for each array in ex2.json: ", times)
file.close()

