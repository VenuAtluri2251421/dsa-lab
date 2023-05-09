class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)
        
def preorder_traversal(node):
    if node is not None:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)
        
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")
        
# Create binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traverse the tree
print("Inorder Traversal:")
inorder_traversal(root)
print("\nPreorder Traversal:")
preorder_traversal(root)
print("\nPostorder Traversal:")
postorder_traversal(root)
