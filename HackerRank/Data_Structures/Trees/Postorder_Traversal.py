#Problem : https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?h_r=next-challenge&h_v=zen

def postOrder(root):
    if root:
        if root.left:
            postOrder(root.left)
        if root.right:
            postOrder(root.right)
        print(root.info, end = ' ')


#rest of code is same as preOrder
