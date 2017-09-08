from .exception import StackEmptyException


class Stack:
    def __init__(self):
        self._data = []

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            raise StackEmptyException

    def push(self, obj):
        self._data.append(obj)

    @property
    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise StackEmptyException

        return self._data[-1]

    def __next__(self):
        if self.is_empty:
            raise StopIteration
        return self.pop()

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        t = to_list(self)
        return ' -> '.join([str(s) for s in t])
        
def get_node(i):
    
    header = Node(0)
    pre = header
    for i in range(1,i):
        pre.next = Node(i)
        pre = pre.next
    return header

def get_cycle_node(i):
    
    head = node = get_node(i)

    while node:
        if node.next is None:
            node.next = head
            break
        node = node.next

        
    return head

def to_list(head):
    t = []
    t.append(head.value)
    node = head.next
    while node and node != head:
        t.append(node.value)
        node = node.next
    
    if node == head:
        t.append('C')
    
    # tmp = ' -> '.join(str(s) for s in t)
    # print(tmp)
    return t
    



def get_stack(i):
    s = Stack()
    for i in range(i):
        s.push(i)
    return s

def print_stack(s):
    print(s._data)    
