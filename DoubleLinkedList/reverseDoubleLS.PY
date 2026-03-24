from collections import deque

class Node:
    def __init__(self,value):
        self.val=value
        self.prev=None
        self.next=None

def createDDL(arr):
    if not arr:
        return None
    
    #create head node
    head=Node(arr[0])
    current_node=head

    #iterate remaining elements
    for i in range(1,len(arr)):
        new_node=Node(arr[i])

        current_node.next=new_node
        new_node.prev=current_node

        current_node=new_node #move pointer

    return head

def main():
    lst=list(map(int,input().split(" ")))
    dll_head=createDDL(lst)
    dll_head_2=createDDL(lst)
    ans=reverse_ddl_brute(dll_head)
    ans2=reverse_ddl(dll_head_2)
    current_node=ans
    print(f'brute force reverse double linked list')
    while current_node is not None:
        print(current_node.val,end=",")
        current_node=current_node.next
    print()
    current_node_opt=ans2
    print(f'optimal reverse double linked list')
    while current_node_opt is not None:
        print(current_node_opt.val,end=",")
        current_node_opt=current_node_opt.next
    print()

    


def reverse_dll(head):
    pass

def reverse_ddl_brute(head):
    stack= deque()

    current=head

    while current is not None:
        stack.append(current.val)
        current=current.next

    current_new=head

    while current_new is not None:
        current_new.val=stack.pop()
        current_new=current_new.next

    return head

def reverse_ddl(head):
    if head.next is None:
        return head
    prev_node=None
    current_node=head
    while current_node is not None:
        front_node=current_node.next
        current_node.next=prev_node
        current_node.prev=front_node
        prev_node=current_node
        current_node=front_node

    return prev_node


if __name__=="__main__":
    main()
    





