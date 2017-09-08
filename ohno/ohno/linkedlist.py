
from .base import *


def remove_kth_node(head, k):
    # 从零开始
    assert isinstance(head, Node)

    if k < 0:
        return head

    if k == 0:
        return head.next

    node = head
    while node:
        if k - 1 == 0:
            node.next = node.next.next if node.next else None
            return head
        k -= 1
        node = node.next

    return head


def remove_last_kth_node(head, k):

    if k <= 0:
        return head
    node = head
    l = 0

    while node:

        k -= 1
        node = node.next
        l += 1

    if k > 0:
        return head
     
    if k == 0:
        return head.next
    
    return remove_kth_node(head, -k)

def reverse(head):
    if head.next is None:
        return head
    
    if head.next.next is None:
        new = head.next
        new.next = head
        head.next = None
        return new
    pre = None
    while head:
        next_ = head.next
        head.next = pre
        pre = head
        head = next_ 
    return pre
        
def killer(head, n):
    if head is None or n < 1:
        return head
    
    i = 0
    while head != head.next:
        if i + 1== n:
            i = 1
            head.next = head.next.next
        else:
            i += 1
        head = head.next
    return head
    