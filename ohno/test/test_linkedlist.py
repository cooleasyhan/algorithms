
from ohno.linkedlist import *
from ohno.base import *


def test_remove_kth_node():
    head = Node(10)
    node = remove_kth_node(head, 1)
    assert node == head

    node = get_node(5)
    print('-' * 10)
    print(to_list(node))
    node = remove_kth_node(node, 5)
    print(to_list(node))
    assert to_list(node) == [0, 1, 2, 3, 4]
    print('-' * 10)
    node = remove_kth_node(node, 4)
    assert to_list(node) == [0, 1, 2, 3]
    print('-' * 10)
    node = remove_kth_node(node, 0)
    assert to_list(node) == [1, 2, 3]


def test_remove_last_kth_node():
    head = get_node(5)
    node = remove_last_kth_node(head, 4)
    assert to_list(node) == [0, 2, 3, 4]

    head = get_node(5)
    node = remove_last_kth_node(head, 5)
    assert to_list(node) == [1, 2, 3, 4]

    head = get_node(5)
    node = remove_last_kth_node(head, 6)
    assert to_list(node) == [0, 1, 2, 3, 4]

def test_reverse():
    head = get_node(5)
    node = reverse(head)
    assert to_list(node) == [4,3,2,1,0]

def test_killer():
    head = get_node(5)
    node = head
    while node:
        if node.next is None:
            node.next = head        
            break
        node = node.next
    
    s = killer(node, 3)
    print(s)
    assert to_list(s)== [3,'C']

    
        