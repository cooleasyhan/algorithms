#%%

def gcd(a,b):
    if a == 0 or b == 0:
        return 0

    if a == b:
        return b

    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(b-a, a)
def main():
    print('gcd: ', gcd(3,9))

if __name__ == '__main__':
    main()
