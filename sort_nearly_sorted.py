'''
Sort a nearly sorted (or K sorted) array
http://www.geeksforgeeks.org/nearly-sorted-algorithm/
'''
from collections import Counter 
from queue import PriorityQueue
c = Counter()


def insertion_sort(arr, size):
    '''
    O(nk)
    '''
    for i in range(1, size):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            c[i] += 1
            j -= 1

        arr[j + 1] = key

def test_insertion_sort():
    arr = [1, 2, 3, 4, 5, 2]
    insertion_sort(arr, len(arr))
    print(arr)
    print(c)


def sort(arr, k, size=None):
    if size is None:
        size = len(arr)
    
    q = PriorityQueue()
    for i in range(k):
        q.put((arr[i],arr[i]))

    for i in range(size):
        if i + k < size:
            q.put((arr[i+k],arr[i+k]))
        min = q.get()[0]
        arr[i] = min
        


def test_sort():
    arr = [9,1,3, 7,2,8,4,]
    sort(arr, 3)
    print(arr)

test_sort()