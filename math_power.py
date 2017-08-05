#%%

"""
2^10 = 4^5 = 16^2*4 = 256*4

"""
def power(x, y):
    res = 1
    while y > 0:
        print(x, y, res)
        if y & 1:
            res = x * res
        
        y = y >> 1
        x = x * x
    return res


print(power(2,10))
print(power(4,5))


#%%
print(1>>1)

print(4 & 1)

#%%
for i in range(10):
    print(i)
    print(i,'>> 1 =', i >>1)
    # print(i,'& 1 =', i & 1)


