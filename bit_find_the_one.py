"""
http://www.geeksforgeeks.org/find-the-element-that-appears-once/
"""
#%%


def get_single(l):
    n = len(l)
    ones = twos = 0
    for i in l:
        print('-' * 50)
        twos = twos | (ones & i)
        ones = ones ^ i
        print('ones', ones, bin(ones))
        print('twos', twos, bin(twos))
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask

        print('ones', ones, bin(ones))
        print('twos', twos, bin(twos))
        print('common_bit_mask', common_bit_mask, bin(common_bit_mask))

    return ones

# print(get_single([5,4,5,5]))

#%%


def get_single2(l):
    max_int_size = 64
    rst = [0] * max_int_size
    for item in l:
        s = bin(item)[2:]
        for idx, data in enumerate(s):
            rst[max_int_size - 1 - idx] += int(data)

    for idx, val in enumerate(rst):
        rst[idx] = val % 3

    print(''.join(['%d' % s for s in rst]))

    print(int(''.join(['%d' % s for s in rst]), 2))


get_single2([2, 2, 2, 3])
