class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # Recursive insert helper
    def __r_insert(self, current_node, value):

        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node

    # Public recursive insert method
    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)


my_tree = BinarySearchTree()

my_tree.r_insert(47)
my_tree.r_insert(46)
my_tree.r_insert(48)

print("root:", my_tree.root.value)
print("root -> left:", my_tree.root.left.value)
print("root -> right:", my_tree.root.right.value)