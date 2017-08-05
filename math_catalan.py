#%%


def store(fun):
    rst = {}

    def wrapper(n):
        if n in rst:
            return rst[n]
        else:
            rst[n] = fun(n)
            return rst[n]

    return wrapper


@store
def catalan(n):
    if n in (0, 1):
        return 1

    rst = 0
    for i in range(n):
        rst += catalan(i) * catalan(n - 1 - i)

    return rst


for i in range(10):
    print(catalan(i))

#%%


def catalan_dp(n):
    if n in (0, 1):
        return 1

    catalan = [0] * n
    catalan[0] = catalan[1] = 1
    for i in range(2, n):
        for j in range(i):
            print(i, '+=', j, '*', i - j - 1)
            catalan[i] += catalan[j] * catalan[i - j - 1]

    print(catalan)


catalan_dp(10)
