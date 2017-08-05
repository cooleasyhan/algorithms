#%%

def add(x, y):
    while y != 0:
        x = x ^ y
        y = x & y << 1


print(-10+100)    


#%%
def multiple_3_point_5(x):
    return (x << 1) + x + (x >> 1)

print(multiple_3_point_5(5  ))

#%%
import sys
print(sys.maxsize * -1>>63)
print(-100000>>300)


print(sys.maxsize)
print(sys.maxsize * -1)
print(len(bin(sys.maxsize)))
print(bin(sys.maxsize))
dir(sys.int_info)
print(sys.int_info.n_unnamed_fields)


#%%
i = int(sys.maxsize)
print(i)
print (type(i << 20000))