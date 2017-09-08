import sys
class Queue:
    def __init__(self, maxsize=0):
        self.front = -1
        self.rear = 0
        self.data = [None] * 10
        self.maxsize = 0

    def is_full(self):
        if self.maxsize == 0:
            return False
        return self.front - self.rear + 1 >= self.maxsize

    def is_empty(self):
        return self.front < self.rear

    def __len__(self):
        return self.front - self.rear + 1

    def _extend(self):
        data_size = len(self.data)
        length = len(self)
        if data_size < length * 2:
            
            print('do_extend')
            self.data.extend([None] * data_size)
        else:
            print('do_move')
            for i in range(length):
                self.data[i] = self.data[i + self.rear]
            
            self.rear = 0
            self.front = length - 1

    def enqueue(self, obj):
        if self.is_full():
            raise Exception('Full')

        try:
            self.data[self.front + 1] = obj
        except IndexError:
            self._extend()
            self.data[self.front + 1] = obj
        self.front += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty')
        self.rear = self.rear + 1
        return self.data[self.rear - 1]


class Deque:
    def __init__(self, max_size=0):
        self.max_size = max_size if max_size != 0 else  sys.maxsize
        self.front = -1
        self.rear = 0
        self.data = [None] * 20
        self.current_size = 20

    def _extend(self):
        if (self.rear == 0 and self.front = self.current_size - 1) or self.rear + 1 == self.front:
            _current_size =( self.current_size * 2 ) if self.current_size * 2 <= self.max_size else self.max_size
            _data = [None] * _current_size
            i = 0
            while self.front != self.rear:
                _data[i] = self.data[self.front]
                self.front += 1
                if self.front == self.current_size:
                    self.front = 0
                i += 1

            self.data = _data
            self.rear = 0
            self.front = i-1
            self.current_size = _current_size
    def insert_front(self, key):
        if self.front = -1:
            self.front = 0
            self.rear = 0
            self.data[0] = key
            return

        self._extend()
        self.front = self.front +  1 % self.current_size
        self.data[self.front] = key

    def delete_front(self, key):
        if self.is_empty():
            raise Exception('Empty')
        self.front = self.front -1
        return self.data[self.front + 1]
        

    def insert_rear(self, key):
        self._extend()
        self.rear = self.rear - 1
        if self.rear == -1:
            self.rear = self.current_size - 1
        self.data[self.rear] = key


    
    def delete_rear(self, key):
        if self.is_empty():
            raise Exception('Empty')
        self.rear = self.rear + 1
        return self.data[self.rear - 1]


    def is_full(self, key):
        return False

    def is_empty(self, key):
        return self.front == -1

    def get_front(self):
        pass

    def get_rear(self):
        pass

        

    
    


def main():

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.enqueue(3)
    q.enqueue(4)
    q.dequeue()
    print(q.front, q.rear, q.data)
    # return
    q = Queue()
    l = list()
    for i in range(1, 1000):
        q.enqueue(i)
        if i % 10 == 0:
            for j in range(9):
                l.append(q.dequeue())

    print(l)
    while True:
        print(q.dequeue())

    # print(q.data)


if __name__ == '__main__':
    main()
