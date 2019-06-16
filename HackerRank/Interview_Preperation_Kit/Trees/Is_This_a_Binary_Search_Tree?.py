#Problem : https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
ipInorder = []
def inOrder(root):
    if root:
        inOrder(root.left)
        ipInorder.append(root.data)
        inOrder(root.right)    
    
def checkBST(root):
    current = root
    flag = 0
    inOrder(current)
    if (len(ipInorder) == len(set(ipInorder))):
        for i in range (1,len(ipInorder)):
            if (ipInorder[i-1] < ipInorder[i]):
                flag += 1
        return (True if flag + 1 == len(ipInorder) else False)
    else:
        return False
