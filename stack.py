class Stack:
    def __init__(self, max_size=1000):
        self.top = -1
        self._data = [None] * 10 if max_size > 10 else max_size
        self.max_size = max_size

    def is_empty(self):
        return self.top == -1

    def _extend_data_list(self):
        size = len(self._data) if len(self._data) * \
            2 <= self.max_size else self.max_size - len(self._data)
        self._data.extend([None] * size)
        print(len(self._data))

    def push(self, data):
        if self.top >= self.max_size - 1:
            raise Exception('Stack Overflow')
        else:
            self.top += 1
            try:
                self._data[self.top] = data
            except IndexError:
                self._extend_data_list()
                self._data[self.top] = data

    def pop(self):
        if self.is_empty():
            raise Exception('Stack Empty')

        self.top -= 1
        return self._data[self.top + 1]


def main():
    s = Stack()
    for i in range(1000):
        s.push(i)

    for i in range(1000):
        s.pop()
    
    print(s.is_empty())


if __name__ == '__main__':
    main()
