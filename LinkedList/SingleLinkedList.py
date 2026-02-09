class Node:
    def __init__(self,val):
        self.val=val
        self.next=next

class SingleLinkedLits:
    def __init__(self):
        self.head=None


node1=Node(5)  #if we print the object we get an address of that object
node2=Node(10)
node3=Node(7)
node4=Node(8)

node1.next=node2
node2.next=node3
node3.next=node4

print(node1.val)
print(node1.next)
print(node2)
print(node1.next.next.next)