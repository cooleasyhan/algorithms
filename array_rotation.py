
#%%
# Version 1 Time: O(n) Space: O(d)
def rotation_array(arr, d, n):
    tmp = arr[:d]
    for i in range(d, n):
        arr[i-d] = arr[i]

    for i in range(d):
        arr[n-i-1] = tmp[d-i-1]
    

arr = list(range(20,0,-1)) 
print(arr)
rotation_array(arr, 4, 20)
print(arr)

#%%
# Version 1 Time: O(dn) Space: O(1)
def left_rotation_one(arr, n):
    tmp = arr[0]
    for i in range(0,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = tmp

def rotation_array2(arr, d, n):
    for i in range(d):
        left_rotation_one(arr, n)
arr = list(range(20,0,-1)) 
print(arr)
rotation_array2(arr, 4, 20)
print(arr)


#%%

from math_gcd import gcd
def left_rotation_d(arr, n, i, d):
    tmp = arr[i]
    for j in range( int(n / d) - 1):
        arr[j * d + i] = arr[(j+1)*d + i]

    arr[n -d + i] = tmp

def left_rotation3(arr, n, d):
    g = gcd(n, d)
    for i in range(int(d/g)):
        for i in range(g):
            print(arr)
            left_rotation_d(arr, n, i, g) 
        print(arr)
arr = list(range(1, 11))
left_rotation3(arr, 10, 6)


#%%

def reverse(arr, b, e):
    l = e - b
    n = l >> 1 
    
    for i in range(n):
        arr[b+i] , arr[e-i-1] = arr[e-i-1], arr[b+i]


def rotation_array4(arr, n, d):
    left = arr[:d]
    right = arr[d:]

    reverse(arr, 0, d)
    print(arr)
    reverse(arr, d, n)
    print(arr)
    reverse(arr,0,n)

arr =list(range(12))
rotation_array4(arr, 12, 4)
print(arr)


#%%
[range(10)[:2] ]+ [range(10)[2:]]


#%%
arr = [3,4,5,6,7,1,2]

def find_pivot(arr, left, right):
    print(left, right)
    if left == right:
        return left
    if left == right -1:
        if arr[left] < arr[right-1]:
            return left
        else:
            return right
    if arr[left] > arr[right-1]:
        n = left + right 
        n = n >> 1
        print(n)
        if arr[left] < arr[n]:
            return find_pivot(arr, n, right)
        else:
            return find_pivot(arr,left, n)
        return n

p = find_pivot(arr, 0, 7)
print(p)