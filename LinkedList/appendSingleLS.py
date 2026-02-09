class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SingleLinkedLits:
    def __init__(self):
        self.head=None
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            curr_node=self.head
            while curr_node.next is not None:
                curr_node=curr_node.next
            curr_node.next=new_node  #here we update last element from linked list with the new address of the new elelment which we created the object of that elemnet
    def traversal(self):
        if self.head is None:
            print('single linked list is empty')
        else:
            current=self.head
            while current is not None:
                print(current.value,end=" ")
                current=current.next  
            print()

    def insert(self,value,position):  # tc --> o(N) and sc --> o(1)
        new_node=Node(value)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            count=0
            prev_node=None
            current_node=self.head
            while current_node is not None and count < position:
                prev_node=current_node
                current_node =current_node.next
                count+=1
            prev_node.next=new_node
            new_node.next=current_node

    def delete(self,val):
        print("enterd in delete")
        current=self.head
        if current.next is not None:
            if current.value==val:
                self.head=current.next
                print("returning here")
                return
            else:
                print("enterd in else")
                found=False
                prev_node=None
                while current is not None:
                    if current.value==val:
                        found=True
                        break
                    prev_node=current
                    current=current.next
                if found:
                    print("deleted the value")
                    prev_node.next=current.next
                    return
                else:
                    print('Node not found')



sll=SingleLinkedLits()
for i in range(5):
    sll.append(i)

sll.insert(100,2)
sll.traversal()
sll.delete(100)
sll.traversal()

