import random


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.colour = 'RED'


class RedBlackTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        rows = []
        level = 0

        def _print(node, level=0):
            prefix = '        ' * (level - 1) + '----' if level > 0 else ''
            rows.append(prefix + str(node.key))
            if node.left:
                _print(node.left, level + 1)
            if node.right:
                _print(node.right, level + 1)

        _print(self.root)
        return '\r\n'.join(rows)

    def insert(self, i):
        if not self.root:
            self.root = Node(i)
            self.root.colour = 'BLACK'
            return

        def _insert(node, i):
            if i < node.key:
                if node.left is None:
                    node.left = Node(i)
                    node.left.parent = node
                    return node
                else:
                    return _insert(node.left, i)
            elif i > node.key:
                if node.right is None:
                    node.right = Node(i)
                    node.right.parent = node
                    return node
                else:
                    return _insert(node. right, i)

        def _p(node):
            return node.parent

        def _uncle(node):
            left = node.parent.parent.left
            right = node.parent.parent.right

            return left if node == right else right

        def _fixup(node):
            # 父节点是黑色，则保持不变即可
            if node.parent.colour == 'BLACK':
                return
            current_node = node
            while current_node.colour == 'RED':
                # 父节点是红色
                # case 1 当前节点的父节点是红色，且当前节点的祖父节点的另一个子节点（叔叔节点）也是红色

                if _p(node).colour == 'RED' and _uncle(node).colour == 'RED':
                    _p(node).colour = 'BLACK'
                    _uncle(node).colour = 'BLACK'
                    _p(_p(node)).colour = 'RED'
                    current_node = _p(_p(node))

            # case2 当前节点的父节点是红色，叔叔节点是黑色，且当前节点是其父节点的右孩子
                elif _p(node).colour == 'RED' and _uncle(node).colour == 'BLACK' and node == _p(node).right:
                    # 将父节点作为轴(当前)节点，左旋， 将当前节点上移，当前节点不变，
                    current_node = _p(node)
                    _left_rotate(current_node)

                # case3 当前节点的父节点是红色，叔叔节点是黑色，且当前节点是其父节点的左孩子
                elif _p(node).colour == 'RED' and _uncle(node).colour == 'BLACK' and node == _p(node).left:
                    # 将祖父节点，标记为红色，将父节点标记为黑色， 祖父节点作为轴（当前）节点，右旋，
                    _p(_p(node)).colour = 'RED'
                    _p(node) = 'BLACK'
                    _right_rotate(_p(_p(node)).colour)
                    current_node = _p(node)

        new_node = _insert(self.root, i)

        _fixup(new_node)


def main():
    rbt = RedBlackTree()
    books = []
    for i in range(100):
        j = random.randint(1, 20)

        if j not in books:
            rbt.insert(j)
        books.append(j)
    print(str(rbt))


if __name__ == '__main__':
    main()
