'''
This is exercise 2 for Assignment 2 ENSF 338
'''

import json
import random
import sys
import timeit

sys.setrecursionlimit(20000) 

def func1(arr, low, high): 
    '''
    
    Arguments: 

    arr (array) = array with all integer values
    low (integer) = index in array, should be the smallest number in arr
    high (integer) = index in array, that should be the highest value in arr
    '''
    if low < high: 
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
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
    # choose a random number, inbetween start and end to avoid reusing same pivot
    # switch out chosen pivot to start index
    # else:
        # there only 2 elements between them 
        # let p equal the first value in that array

    if (end - start >= 2):
        pivot_index = random.randint(start, end)
        array[start], array[pivot_index]= array[pivot_index], array[start]
        p = array[start]

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


filename_r = "/Users/owner/Documents/YEAR2/W23_Y2/ENSF338/Assignment2/ex2.json"
filename_w = "/Users/owner/Documents/YEAR2/W23_Y2/ENSF338/Assignment2/ex2.5.json"
times =[]
times_op =[]

with open(filename_r, "r") as file:
    data = json.load(file)

    #data has 10 arrays 
    i = 0 
    for items in data:
        executed_time = timeit.timeit(lambda:func1(data[i], 0, (len(data[i]) - 1)) , number =1)
        times.append(executed_time)
        i = i + 1

with open(filename_w, "w") as write:
    json.dump(data,write)
write.close()

with open(filename_w, "r") as file_op:
    alter = json.load(file_op)

    i = 0 
    for items in data:
        executed_time = timeit.timeit(lambda:func1(alter[i], 0, (len(alter[i]) - 1)) , number =1)
        times_op.append(executed_time)
        i = i + 1

print("Timing for each array in ex2.json: ", times)
print("Timing for each altered arrays: ", times_op)

file.close()
file_op.close()
