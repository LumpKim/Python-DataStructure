# code by http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)

        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data)

            else:
                node.right = self.insert_value(node.right, data)
        return node

    def find(self, key):
        return self.find_value(self.root, key)

    def find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.find_value(root.left, key)
        else:
            return self.find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self.delete_value(self.root, key)
        return deleted

    def delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.reft
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.delete_value(node.left, key)
        else:
            node.right, deleted = self.delete_value(node.right, key)
        return node, deleted


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False