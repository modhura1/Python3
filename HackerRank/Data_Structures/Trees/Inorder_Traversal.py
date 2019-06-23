#Problem : https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def inOrder(root):
    if root:
        if root.left:
            inOrder(root.left)
        print(root.info, end = ' ')
        if root.right:
            inOrder(root.right)
            
#rest of the code is same as preOrder
