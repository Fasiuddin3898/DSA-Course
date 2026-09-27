# This is the code to build a binary tree from the given array remember the binary tree has 
# atmost two childern

from queue import Queue

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree(values):
    if not values:
        return None
    root=TreeNode(values[0])
    ele_queue=Queue([root])
    i=0

    while i < len(values) and ele_queue.qsize():

        current_node = ele_queue.popleft()
        i+=1
        # left tree
        if i < len(values) and values[i] is not None:
            current_node.left=values[i]
            ele_queue.put(current_node.left)

        i+=1
        # right tree
        if i< len(values) and values[i] is not None:
            current_node.right=values[i]
            ele_queue.put(current_node.right)

        i+=1

    return root

def height_of_BT(values):
    if not values:
        return
    rootNode=build_tree(values)
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








