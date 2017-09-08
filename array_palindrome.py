def transfer_to_palindrome(l):
    i = 0
    j = len(l) - 1
    rst = [None] * len(l)

    while i <= j:
        if l[i] == l[j]:
            rst[i] = rst[j]= l[i]
            i += 1
            j -= 1


        if l[i] < l[j] and i + 1 <= j:
            l[i+1] = l[i] + l[i+1]
            i += 1
        elif l[i] > l[j] and j -1 >= i:
            l[j - 1] = l[j] + l[j-1]
            j -= 1
    return  [i for i in rst if i]


def main():
    l = [1,1,1,3]
    rst = transfer_to_palindrome([1,1,1,3])
    print(rst)
    print(len(l) - len(rst))


if __name__ == '__main__':
    main()
        


