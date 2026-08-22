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

    # Find minimum value
    def min_value(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    # Recursive delete helper
    def __delete_node(self, current_node, value):

        if current_node is None:
            return None

        if value < current_node.value:

            current_node.left = self.__delete_node(
                current_node.left, value
            )

        elif value > current_node.value:

            current_node.right = self.__delete_node(
                current_node.right, value
            )

        else:
            # Case 1: No children
            if current_node.left is None and current_node.right is None:
                return None

            # Case 2: Only right child
            elif current_node.left is None:
                current_node = current_node.right

            # Case 3: Only left child
            elif current_node.right is None:
                current_node = current_node.left

            # Case 4: Two children
            else:
                sub_tree_min = self.min_value(current_node.right)

                current_node.value = sub_tree_min

                current_node.right = self.__delete_node(
                    current_node.right,
                    sub_tree_min
                )

        return current_node

    # Public delete method
    def delete(self, value):
        self.root = self.__delete_node(self.root, value)


# Create BST
my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(46)
my_tree.insert(48)

print("Before deleting:")
print("Root:", my_tree.root.value)
print("Left:", my_tree.root.left.value)
print("Right:", my_tree.root.right.value)

# Delete 46
my_tree.delete(46)

print("\nAfter deleting 46:")
print("Root:", my_tree.root.value)

if my_tree.root.left is None:
    print("Left: None")

if my_tree.root.right is not None:
    print("Right:", my_tree.root.right.value)