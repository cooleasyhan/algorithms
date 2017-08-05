#%%
def print_divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


print_divisors(100)

#%%
from math import sqrt


def print_divesors2(n):
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                print(i)
            else:
                print(i)
                print(int(n / i))


print_divesors2(100)
