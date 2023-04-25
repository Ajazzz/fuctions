import numpy as np

def create_array(n):
    return np.arange(n)

''' Example usage: '''
arr = create_array(5)
print(arr)   # Output: [0 1 2 3 4]


''' Calculating the mean of an array: '''

import numpy as np

def calculate_mean(arr):
    return np.mean(arr)

''' Example usage: '''
arr = np.array([1, 2, 3, 4, 5])
mean = calculate_mean(arr)
print(mean)   # Output: 3.0


''' Reshaping an array:'''
import numpy as np

def reshape_array(arr, shape):
    return np.reshape(arr, shape)

# Example usage:
arr = np.array([1, 2, 3, 4, 5, 6])
new_shape = (2, 3)
new_arr = reshape_array(arr, new_shape)
print(new_arr)   # Output: [[1 2 3], [4 5 6]]



#Count Occurrences
#returns the number of times the element x appears in the given array using the count method.
#here are sone examples;

def count_occurrences(arr, x):
    return arr.count(x)
    
arr=[1,2,3,4,1,3,4]
x=1
count_occurrences(arr, x)
print(count_occurrences)  # Output: 2


#Reverse Array 
#reverses the order of the elements in the given array using the reverse method.

def reverse_arr(arr):
    arr.reverse()
    return arr
arr=[1,2,3,4,1,3,4]    
reverse_arr(arr)  # Output: [4, 3, 1, 4, 3, 2, 1]


Remove duplicates 
#removes all duplicate elements from the given array using a combination of the list and set data types.

arr=[1,2,3,4,1,3,4]
def remove_duplicates(arr):
    return list(set(arr))

remove_duplicates(arr)  # Output:  [1, 2, 3, 4]


