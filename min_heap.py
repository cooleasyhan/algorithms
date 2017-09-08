from queue import PriorityQueue
import copy


class MinHeap:
    def __init__(self,  max_size=0):
        self.max_size = max_size
        self.data = list()

    def __len__(self):
        return len(self.data)

    def put(self, kv):
        def _siftup(i):
            p = (i - 1) >> 1
            # u =  ((p + 1) * 2 ) - 1  if i = (p + 1) * 2  else  (p + 1) * 2
            if self.data[i] < self.data[p]:
                self.data[p], self.data[i] = self.data[i], self.data[p]
                return p
            return None

        # key = kv[0]
        self.data.append(kv)
        i = len(self.data) - 1
        while i > 0:
            i = _siftup(i)
            if not i:
                break

    def pop(self):
        def _siftdown(i):
            left = (i + 1) * 2 - 1 if (i + 1) * \
                2 - 1 < len(self.data) else None
            right = (i + 1) * 2 if (i + 1) * 2 < len(self.data) else None
            _min = i

            if left is not None:
                if self.data[left] < self.data[_min]:
                    _min = left

            if right is not None:
                if self.data[right] < self.data[_min]:
                    _min = right

            if _min != i:
                self.data[_min], self.data[i] = self.data[i], self.data[_min]
                return _min
            else:
                return None

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        item = self.data.pop()

        i = 0
        while i < len(self.data):
            i = _siftdown(i)
            if i is None:
                break

        return item

    def sort(self):
        tmp = copy.copy(self.data)
        while self.data:
            yield self.pop()


heap = MinHeap()
pq = PriorityQueue()
import random
for i in range(100):
    j = random.randint(1, 100)
    heap.put(j)
    pq.put((j, j))


print(heap.data)
print([i[0] for i in pq.queue])

i = heap.pop()
print(heap.data)
i = pq.get()
print([i[0] for i in pq.queue])
# for i in heap.sort():
#     print(i)