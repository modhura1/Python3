#Problem : https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees


    current = root
    if current.data in ipList:
        return False
    else:
        ipList.append(current.data)
        #print(ipList)
        if (current.left == None and current.right == None):
            return True
        elif (current.left.data < current.data and current.right.data > current.data):
            checkBST(current.left)
            checkBST(current.right)
