'''
Implementing a simple binary search in python.
It takes as input list and the desired item and returns the index
'''

def binary_search(list, item):
    low = 0 # set at index 0
    high = len(list) - 1 # set at the highest index

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


'''
Testing the binary_search
'''
if __name__ == "__main__":
    print binary_search([1,2,3,4,5,6],5) # should return 2
