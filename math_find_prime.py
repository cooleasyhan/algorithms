#%%
def sieve_of_eratosthenes(n):
    l = [True] * (n+1)

    l[0] = False
    l[1] = False
    l[2] = True
    i = 2
    while i <= n:
        if l[i] is False:
            i += 1
            continue
        j = 2 * i
        while j < n + 1:
            l[j] = False
            j += i
        i += 1
        
    print([idx for idx,  i in enumerate(l) if i])

sieve_of_eratosthenes(101)