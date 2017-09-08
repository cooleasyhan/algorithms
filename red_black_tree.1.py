RED = True
BLACK = False

class Node:
    def __init__(self, key, value, count, color):
        self.key = key
        self.value = value
        self.count = count
        self.color = color
        self.left = None
        self.right = None

    def __len__(self):
        return self.count


class RedBlackBST:
    def __str__(self):
        rows = []
        level = 0

        def _print(node, level=0):
            prefix = '        ' * (level - 1) + '----' if level > 0 else ''
            rows.append(prefix + str(node.key) + ('R' if node.color else ''))
            if node.left:
                _print(node.left, level + 1)
            if node.right:
                _print(node.right, level + 1)

        _print(self.root)
        return '\r\n'.join(rows)

    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False

        return node.color == RED

    def rotate_left(self, node):
        '''
        自身左移， 右子树上移
                |
            E
        /         \
    x<E          S
                /      \
                /          \
        E< x <S      x>S

        ||
        ||
            |
            S
            /   \
        E     x>S
        /     \
    x <E   (E,S)
        '''

        s = node.right
        node.right = s.left
        s.left = node
        s.color = node.color
        node.color = RED

        return s

    def rotate_right(self, node):
        '''
        左子树上移，自身右移
                |
                S
            /   \
        E      >S
        /    \
    <E    (E S)

            ||
            ||
                | 
                E
                /      \
            <E       S
                    /      \
                (E,S)     >S

        '''
        left = node.left
        node.left = left.right
        left.right = node

        left.color = node.color
        node.color = RED

        return left

    def flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def _put(self, node, key, val):
        if node is None:
            return Node(key, val, 1, RED)

        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.value = val

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        node.count = len(node.left) if node.left else 0 + len(node.right) if node.right else 0 + 1
        return node

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
        self.root.color = BLACK

def main():
    t = RedBlackBST()
    for i in range(1,100000):
        t.put(i, i)
    print(str(t))

if __name__ == '__main__':
    main()
    