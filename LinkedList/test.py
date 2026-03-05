class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SingleLinkedLits:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head is None:
            print("Single lined list is empty")
            return
        else:
            curr_node=self.head
            while curr_node is not None:
                print(curr_node.next,end=" ")
                curr_node=curr_node.next
        print()
        return
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            curr_node=self.head
            while curr_node.next is not None:
                curr_node=curr_node.next
            curr_node.next=new_node
    def inser(self,value,position):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            if position==0:
                new_node.next=self.head
                self.head=new_node
            else:
                prev_node=0
                curr_node=self.head
                count=0
                while curr_node is not None and count<position:
                    prev_node=curr_node
                    curr_node=curr_node.next
                    count+=1
                prev_node.next=new_node
                new_node.next=curr_node

    def delete(self,value):
        curr_node=self.head
        if curr_node.next is not None:
            if curr_node.value==value:
                self.head=curr_node.next
                return
            else:
                prev_node=None
                found=False
                while curr_node is not None:
                    if curr_node.value==value:
                        found=True
                        break
                    prev_node=curr_node
                    curr_node=curr_node.next
                if found:
                    prev_node.next=curr_node.next
                    del curr_node
                else:
                    print(f'given value is not found')

            
