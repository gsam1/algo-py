import time

start_time = time.time()

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)



print quicksort([4,9,1,3,2,19,6,14])

print time.time() - start_time
