import time
import random
start_time = time.time()

RANGE = 2**18

def binary_search(array, item):
    '''Binary search returns the index of the item in an array (list in python). Binary search takes O(log2 n) to run.
    That means it takes the logarithm2 of the number of items in the array operations to run.
    For example, if an array has 100 items in it, log2 of 100 is 7, so it would take at most 7 operations. '''
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
my_list = [i for i in range(RANGE)]
# print(my_list)
print(binary_search(my_list, random.randint(0, RANGE)))
print(f'Seconds: {time.time() - start_time}')
print(binary_search(my_list, random.randint(0, RANGE)))
print(f'Seconds: {time.time() - start_time}')