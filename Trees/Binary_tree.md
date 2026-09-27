# What is Binary Tree?
A tree which has atmost 2 childrens is known as binary tree
# Binary tree has
Root, Nodes, Children, Parent, Ancestors, Leaf Node, Subtree

**Leaf Node: A node with zero children is called Leaf Node.**

1. Full Binary Tree: All nodes should have 2 or 0 childern then it is called as Full Binary Tree (Note: If Node has one children then it is not a Full Binary Tree )

2. Complete Binary Tree: All levels must be full except the last level and the last level has all the nodes to extreme left as possible 

3. Perfect Binary Tree: All leaf node are at same level and all non-leaf node must have 2 children

4. Balanced Binary Tree: Height difference between left and right subtree at any node must be at max 1

5. Degenrate Binary Tree: Every node has only one children

# How to write the code for Binary Tree

# Different Traversal

1. DFS(Depth First Search)  In all the search techniquies we use recurssion

**Preorder** [Root-Left-Right]
-> Code to print the preorder values from a tree [root-left-right]
**Remember pre means print the root first**

def preorder(Node):
    if Node==None:
        return
    print(Node.val, end=" ")
    preorder(Node.left)
    preorder(Node.right)

preorder(root)

In above time complexity is O(N) and space complexity is the stack is filled with the height of the binary tree O(H) where H is the heigt of the binary tree

**In-order**  [left-root-right]
-> Code to print the In-order elements from the tree [left-root-right]
**Remeber in means root has to be in between the left and right**

def inorder(Node):
    if Node ==None:
        return
    inorder(Node.left)
    print(Node.val,end=" ")
    inorder(Node.right)

inorder(root)

In above time complexity is O(N) and space complexity is the stack is filled with the height of the binary tree O(H) where H is the heigt of the binary tree

**post-order** [left-right-root]
-> Code to print the post order elements from the tree [left-right-root]
**Remember post means print the root after the left and right**

def postorder(Node):
    if Node==None:
        return
    postorder(Node.left)
    postorder(Node.right)
    print(Node.val,end=" ")

postorder(root)

In above time complexity is O(N) and space complexity is the stack is filled with the height of the binary tree O(H) where H is the heigt of the binary tree



2. BFS (Breadth First Search)  In this we use loop [Level-Order-Traversal]
horizontal is called as Breadth (we print horizental level wise elements from the tree)
Steps to traverse level order traversal
1. take the queue and insert the root element in it
2. run the loop until the queue is empty and keep adding the queue element object in to the queue by checking its left and right before adding print the element value
3. While poping from the queue print the elemnts first and add that elemnets left and right in to the queue

queue_elemnets=[]
results=[]

queue_elemnets.append(root)

while len(queue_elemnets) != 0:
    temp=queue_elemnets.pop()
    results.append(temp.val)
    if temp.left:
        queue_elemnets.add(temp.left)
    if temp.right:
        queue_elemnets.add(temp.right)

print(results) 


**Another metod to write the code**

def level_order(Node):
    result=[]
    queue=deque([])
    queue.append(Node)

    while len(queue) != 0:
        e=queue.popleft()
        result.append(e.val)
        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
    return result 
level_order(root)

Here time and space complexity is O(N) and O(N)









