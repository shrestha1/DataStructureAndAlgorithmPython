from xml.dom.minidom import Element

from torch import le


class BinarySearchTree:
    def __init__(self, data) -> None:
        self.data = data 
        self.right = None
        self.left = None
    
    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        element = []

        #Add left 
        if self.left:
            element+=self.left.inorder_traversal()

        #Add root
        element.append(self.data)

        #Add right
        if self.right:
            element+=self.right.inorder_traversal()

        return element

    def preorder_traversal(self):
        element = []

        #Add root 
        element.append(self.data)

        #Add left
        if self.left:
            element+=self.left.preorder_traversal()

        #Add right
        if self.right:
            element+=self.left.preorder_traversal()
        
        return element

    def postorder_traversal(self):
        element = []

        #Add left
        if self.left:
            element+=self.left.postorder_traversal()

        #Add right
        if self.right:
            element+=self.right.postorder_traversal()

        #Add root
        element.append(self)

    def find_max(self):
        if self.right:
            self.right.find_max()
        return self.data
    
    def find_min(self):
        if self.left:
            self.left.find_min()
        return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self



def build_tree(elements):
    root = BinarySearchTree(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])

    print(numbers_tree.inorder_traversal())
    # print(numbers_tree.preorder_traversal())
    # print(numbers_tree.postorder_traversal())
    # print(numbers_tree.search(20))
    # print(numbers_tree.calculate_sum())
    numbers_tree.delete(20)

    print(numbers_tree.inorder_traversal())

