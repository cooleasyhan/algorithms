from .base import Stack, get_stack, print_stack
from .exception import StackEmptyException


class MinStack:
    '''
    实现 一个 特殊 的 栈， 在 实现 栈 的 基本功 能 的 基础上， 再 实现 返回 栈 中最 小 元素 的 操作。
    '''

    def __init__(self):
        self.stack = Stack()
        self.minstack = Stack()

    def push(self, obj):
        if self.stack.is_empty:
            self.minstack.push(obj)
        elif obj < self.minstack.peek():
            self.minstack.push(obj)

        self.stack.push(obj)

    def pop(self):
        obj = self.stack.pop()
        if obj == self.get_min():
            self.minstack.pop()
        return obj

    def get_min(self):
        return self.minstack.peek()


class TwoStackQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def add(self, obj):
        self.push_stack.push(obj)

    def _move(self):
        while not self.push_stack.is_empty:
            tmp = self.push_stack.pop()
            self.pop_stack.push(tmp)

    def poll(self):
        if self.pop_stack.is_empty:
            self._move()
        return self.pop_stack.pop()

    def peak(self):
        if self.pop_stack.is_empty:
            self._move()
        return self.pop_stack.peek()


def remove_last_item(stack):
    obj = stack.pop()

    if stack.is_empty:
        return obj

    last = remove_last_item(stack)
    stack.push(obj)
    return last


def reverse_stack(stack):
    if stack.is_empty:
        return
    obj = remove_last_item(stack)
    reverse_stack(stack)
    stack.push(obj)


def sort_stack_by_stack(stack):
    helper = Stack()
    while not stack.is_empty:
        obj = stack.pop()
        if helper.is_empty:
            helper.push(obj)
        while not helper.is_empty and obj > helper.peek:
            tmp = helper.pop()
            stack.push(tmp)

        helper.push(obj)


s = get_stack(10)
print_stack(s)
reverse_stack(s)
print_stack(s)
