"""
    PreOrder Traversal Question of HackerRank
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    
    if root == None:
        return

    out_str = "" + '{}'.format(root.info)
    
    # print left
    if root.left:
        out_str += ' {}'.format(preOrder(root.left))
        
    # print right
    if root.right:
        out_str += ' {}'.format(preOrder(root.right))
        
    return out_str

tree = BinarySearchTree()
t = [1, 2, 5, 3, 6, 4]

# arr = list(map(int, input().split()))

for i in t:
    tree.create(i)

print(preOrder(tree.root))