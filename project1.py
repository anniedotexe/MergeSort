'''
Annie Wu
Python Project 1
CS 3750.02
28 Sept 2018
'''

import random

#create array of 20 random integers
array = random.sample(range(1, 101), 20)
#low is first index of the array
low = 0
#high is the last index, which is length of the array -1
high = len(array) - 1

#print original array
print("Random Array: ")
#for all indices in array
for i in array:
    #print index i with a space after it
    print(i, end = " ")

#function for quick sort
def quickSort(array, low, high):
    #if low index is less than high index
    if low < high:
        #create pivot index
        pivot = partition(array, low, high)
        #recursively sort elements before the pivot
        quickSort(array, low, pivot)
        #recursively sort the elements after the pivot
        quickSort(array, pivot + 1, high)

#function for partitioning the array    
def partition(array, low, high):
    #left pointer is low
    left = low
    #right pointer is high
    right = high
    #pivot index is the left pointer
    pivot = array[left]

    #while the left pointer is <= right pointer
    while left <= right:
        #while the left pointer's item is less than the pivot
        #and the left pointer is not at the end of the array
        while array[left] < pivot and left < high:
            #increment the left pointer
            left = left + 1
        #while the right pointer's item is greater than the pivot
        #and the right pointer is not at the beginning of the array
        while array[right] > pivot and right > low:
            #decrement the right pointer
            right = right - 1
        #if the left pointer is less than the right pointer
        if left < right:
            #swap the left and right pointer's items
            array[left], array[right] = array[right], array[left]
        #else left pointer >= right pointer
        else:
            #return the right element
            return right

#call quickSort function
quickSort(array, low, high)

#print sorted array
print("\nSorted Array: ")
#for all indices in array
for i in array:
    #print index i with a space after it
    print(i, end = " ")
