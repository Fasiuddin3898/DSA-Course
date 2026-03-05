class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_head(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def append(self,value):   #append at the end of linked list
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current

    def inser(self,value,position):
        new_node=Node(value)
        if position==0:
            self.insert_at_head(value)
            return
        curr_node=self.head
        count=0
        while curr_node and count < position-1:
            curr_node=curr_node.next
            count+=1
        if curr_node is None:
            print(f'position out of bound')
            return
        new_node.next=curr_node.next
        new_node.prev=curr_node
        if curr_node.next:    #checking if it is not the last node
            curr_node.next.prev=new_node
        curr_node.next=new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        if not current:
            return

        while current.next:
            current = current.next

        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

    def delete_head(self):
        if not self.head:
            print(f'List is empty')
            return
        if self.head.next is None:
            self.head =None
            return
        new_node=self.head.next
        new_node.prev=None
        self.head=new_node

    def delte_last(self):
        if self.head is None:
            print("No element is present")
            return
        if self.head.next is None:
            self.head=None
            return
        curr_node=self.head
        while curr_node.next is not None:
            curr_node=curr_node.next
        prev_node=curr_node.prev
        prev_node.next=None

    def delete_in_bw(self,value):
        if self.head is None:
            print("No element is present")
            return
        curr_node=self.head
        #travel to find the node just before we delete it
        while curr_node and curr_node.value != value:
            curr_node=curr_node.next
        if curr_node is None:
            print(f'value not found')
            return
        if curr_node.prev is None: #delte head
            self.head=curr_node.next
            if self.head:
                self.head.prev=None

        # delete last node
        elif curr_node.next is None:
            curr_node.prev.next=None

        else:
            curr_node.prev.next=curr_node.next
            curr_node.next.prev=curr_node.prev
        del curr_node
            

def main():
    lst = [1,2,3,4,5,6]
    dll = DoubleLinkedList()
    # Build doubly linked list using append
    for value in lst:
        dll.append(value)
    print("Forward Traversal:")
    dll.display_forward()
    print("Backward Traversal:")
    dll.display_backward()

if __name__=="__main__":
    main()