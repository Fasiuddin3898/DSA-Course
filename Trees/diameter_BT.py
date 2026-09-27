from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree(values):
    if not values:
        return None
    root=Node(values[0])
    queue=deque([root])
    i=0
    while queue and i<len(values):
        curr_node=queue.popleft()
        i+=1
        if i<len(values) and values[i] is not None:
            curr_node.left=Node(values[i])
            queue.append(curr_node.left)
        i+=1
        if i<len(values) and values[i] is not None:
            curr_node.right=Node(values[i])
            queue.append(curr_node.right)

    return root

diameter=0


def traverse(root):
    global diameter
    if root == None:
        return 0
    left_height=traverse(root.left)
    right_height=traverse(root.right)
    diameter=max(diameter,left_height+right_height)
    return 1+max(left_height,right_height)

def main():
    arr=[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    root=build_tree(arr)
    traverse(root)
    print(f'diameter {diameter}')
    return diameter

if __name__=="__main__":
    main()





    