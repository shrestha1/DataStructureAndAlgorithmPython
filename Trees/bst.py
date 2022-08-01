from logging import root
import numbers


class BinarySearchTree:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add node to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # add node to the right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        elements = []
        
        # visit left node
        if self.left:
            elements += self.left.inorder_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit right node
        if self.right:
            elements += self.right.inorder_traversal()
        
        return elements

    def preorder_traversal(self):
        elements = []
        
        # add root node 
        # -- code here --
        elements.append(self.data)

        # add left node 
        # -- code here --
        if self.left:
            elements+=self.left.preorder_traversal()

        # add right node
        # -- code here --
        if self.right:
            elements+=self.right.preorder_traversal()
        
        return elements

    def postorder_traversal(self):
        elements = []
        
        # add left node
        # -- code here --
        if self.left:
            elements += self.left.postorder_traversal()
        
        # add right node
        # -- code here --
        if self.right:
            elements += self.right.postorder_traversal()

        # add root node 
        # -- code here --
        elements.append(self.data)

        return elements
    
    def search(self, val):
        if self.data == val:
            print(self.data)
            return True
        
        # Search in left SubTree
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False

        # Search in right SubTree
        if val > self.data:
            if self.right:
                self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)

    # print(numbers_tree.inorder_traversal())
    # print(numbers_tree.preorder_traversal())
    # print(numbers_tree.postorder_traversal())
    print(numbers_tree.search(22))