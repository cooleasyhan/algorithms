# -*- encoding:utf-8 -*-
class Bitmap():
    ARRAY_SIZE = 64 - 1

    def __init__(self, max):
        self.size = int((max + Bitmap.ARRAY_SIZE - 1) / Bitmap.ARRAY_SIZE)
        self.array = [0 for i in range(self.size)]

    def bitindex(self, num):
        '确定数组中元素的位索引'
        return num % Bitmap.ARRAY_SIZE

    def set_1(self, num):
        '将元素所在的位置1'
        elemindex = int(num / Bitmap.ARRAY_SIZE)
        byteindex = self.bitindex(num)
        ele = self.array[elemindex]
        self.array[elemindex] = ele | (1 << byteindex)

    def test_1(self, i):
        '检测元素存在的位置'
        elemindex = int(i / Bitmap.ARRAY_SIZE)
        byteindex = self.bitindex(i)
        if self.array[elemindex] & (1 << byteindex):
            return True
        return False


def is_contain(A, B):
    a = Bitmap(100)
    b = Bitmap(100)

    for i in A:
        a.set_1(ord(i))

    for i in B:
        if a.test_1(ord(i)):
            return True

    return False


if __name__ == '__main__':
    print(is_contain('ABCDE', 'ED'))
    print(is_contain('ABCDE', 'gf'))

    A = '2222ABCD'
    B = '11ABCD'

    la = len(A)
    lb = len(B)
    rst = []
    for i in range(min((la, lb))):
        if A[i] == B[i]:
            rst.append(A[i])
        else:
            break
    print(''.join(rst))

    rst = []
    for i in range(1, min((la, lb))+1):
        print(-i)
        if A[-i] == B[-i]:
            rst.append(A[-i])
        else:
            break

    print(''.join( reversed(rst)))
