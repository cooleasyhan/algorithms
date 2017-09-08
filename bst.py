'''
Binary Search Tree, is a node-based binary tree data structure which has the following properties:

    The left subtree of a node contains only nodes with keys less than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.
    There must be no duplicate nodes.

Insertion of a key:
A new key is always inserted at leaf. We start searching a key from root till we hit a leaf node. 
Once a leaf node is found, the new node is added as a child of the leaf node.
'''
from collections import deque
def caculte_depts(root):
    if root is None:
        return 0
    if  hasattr(root, 'dept') :
        return root.dept
    else:
        left_dept  = caculte_depts(root.left) + 1
        right_dept = caculte_depts(root.right)  + 1
        root.dept = max([left_dept, right_dept])
        return root.dept

def print_tree(root):
    max_dept = caculte_depts(root)
    book = []
    q = deque()
    q.append(root)
    while q:
        tmp = q.popleft()
        val = tmp.data
        if val not in book:
            book.append(val)
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)
        
    print(book)

def print_tree2(root, level=0):
    rows = []
    def _print_tree2(root, level=0):
        if root:
            l = 4 if level > 0 else 0
            rows.append('  ' *  (4 * (level-1)) + '-' * l  + str(root.data))
            _print_tree2(root.left, level=level+1)
            _print_tree2(root.right, level=level+1)

    _print_tree2(root, level)
    for row in rows:
        print(row)

    




    

        


    

# ----10----
# ---/--\---
# --30--40--

class Node(object):
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def travel(self, node='ROOT'):
        if node == 'ROOT':
            node = self.root

        if node:
            self.travel(node.left)
            print(node.data)
            self.travel(node.right)

    def search(self, i):
        def _search(node, i):
            if not node:
                raise Exception('Not Found')
            print('----', node.data)
            if node.data == i:
                return node
            elif node.data > i:
                return _search(node.left, i)
            else:
                return _search(node.right, i)

        return _search(self.root, i)

    def min_node(self, node):
        m = node
        while node.left:
            m = node.left

        return m

    def delete(self, i):
        def _find_min(node):
            if node.left is None:
                return node
            else:
                return _find_min(node.left)

        def _delete(node, i):
            if node is None:
                return node
            if i < node.data:
                node.left = _delete(node.left, i)
            elif i > node.data:
                node.right = _delete(node.right, i)
            else:
                if node.left is None:
                    tmp = node.right
                    node = None
                    return tmp
                elif node.right is None:
                    tmp = node.left
                    node = None
                    return tmp
                else:
                    min_node = _find_min(node.right)
                    print('min_node', min_node.data)
                    node.data = min_node.data
                    node.right = _delete(node.right, min_node.data)
                
            return node
        _delete(self.root, i)

    def add(self, i):
        def _add(node, i):
            if node.data > i:
                if node.left is None:
                    node.left = Node(i)
                else:
                    _add(node.left, i)
            elif node.data < i:
                if node.right is None:
                    node.right = Node(i)
                else:
                    _add(node.right, i)
            else:
                return
                # raise Exception('Duplicate Key')

        if self.root is None:
            self.root = Node(i)
            return
        else:
            _add(self.root, i)


def main():

    import random
    b = BST()
    for i in range(1000):
        b.add(random.randint(1, 20))
    # b.travel()

    b.search(10)
    print_tree(b.root)
    print_tree2(b.root)
    b.delete(10)
    print_tree(b.root)
    print_tree2(b.root) 

    # b.search(10)

#     b = BST()
#     nodes = []
#     for i in range(10):
#         nodes.append(Node(i))
    
#     b.root = nodes[6]
#     b.root.left = nodes[4]
#     b.root.right = nodes[8]
#     b.root.left.left = nodes[2]
#     b.root.left.right = nodes[5]
#     b.root.left.left.left = nodes[1]
#     b.root.left.left.right = nodes[3]
#     b.root.right.left = nodes[7]
#     b.root.right.right = nodes[9]

#     print_tree(b.root)
#     print_tree2(b.root)
# #       6
#     4     8
#   2  5  7  9
#  1 3

if __name__ == '__main__':
    main()
