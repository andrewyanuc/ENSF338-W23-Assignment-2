'''
This is exercise 2 for Assignment 2 ENSF 338
'''

import json
import sys
import timeit

sys.setrecursionlimit(20000) 

filename = "/Users/owner/Documents/YEAR2/W23_Y2/ENSF338/Assignment2/ex2.json"
inserted_array =[]

with open(filename, "r") as file:
    data = json.load(file)
    #data has 10 arrays 
    i = 0 
    for items in data:
        j = 0
        while j < len(data[i]):
            inserted_array.append(data[i][j])
            j = j +1
        i = i + 1


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


executed_time = timeit.timeit(lambda:func1(inserted_array, 0, (len(inserted_array) - 1)) , number =1)
print(executed_time)

file.close()

