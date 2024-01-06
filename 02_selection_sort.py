# Selection sort works in O(n^2) time because each element of the array
# has to be touched n times for a list of n length, so n * n or n^2
import time
import random
start_time = time.time()
RANGE = 2**8

def find_smallest(array):
    '''Finds the smallest element in an array and
    returns its index'''
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    '''Sorts the passed array and returns a copy of it'''
    new_array = list()
    copied_array = list(array)
    for i in range(len(copied_array)):
        smallest = find_smallest(copied_array)
        new_array.append(copied_array.pop(smallest))
    return new_array

# Create a random list of unsorted integers
unsorted_list = list()
for i in range(RANGE):
    unsorted_list.append(random.randint(0, RANGE))

print(f'\nLast 5 entries in random list: {unsorted_list[-5:]}')
print(f'Seconds: {time.time() - start_time}')
print(f'\nSorted list: {selection_sort(unsorted_list)}')
print(f'Seconds: {time.time() - start_time}')
