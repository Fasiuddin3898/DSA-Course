# This is leet code 104 where we need to find out the maximum height of the tree

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_binary_tree(values):
    if not values:
        return None
    root=Node(values[0])
    queue=[root]
    i=1
    while queue and i<len(values):
        current=queue.pop()

        # left child
        if i<len(values) and values[i] is not None:
            current.left=Node(values[i])
            queue.append(current.left)

        i+=1

        # right child
        if i<len(values) and values[i] is not None:
            current.right=Node(values[i])
            queue.append(current.right)

        i+=1

    return root

def height_of_BT(values):
    if not values:
        return
    rootNode=build_binary_tree(values)
    ans=traverse(rootNode)
    print(f'height of a binary tree is {ans}')
    return ans


def traverse(root):
    if root==None:
        return 0
    leftHeight=traverse(root.left)
    rightHeight=traverse(root.right)
    return 1+max(leftHeight,rightHeight)

if __name__=="__main__":
    values=[1,None,2]
    height_of_BT(values)






        