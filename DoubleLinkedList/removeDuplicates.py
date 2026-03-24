#Remove duplicates from sorted double linked list

class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        self.prev=None

class NodeSingle:
    def __init__(self,value):
        self.val=value
        self.next=None

def ssl(arr):
    head=NodeSingle(arr[0])
    curr_node=head
    for i in range(1,len(arr)):
        new_node=NodeSingle(arr[i])
        curr_node.next=new_node
    return head

def removeduplicatesSSL(head):
    curr_node=head
    prev_node=None
    set_value=set()
    while curr_node:
        value=curr_node.val
        if value in set_value:
            prev_node.next=curr_node.next
        else:
            set_value.add(value)
            prev_node=curr_node

        curr_node=curr_node.next

    return head


def ddl(arr):
    head=Node(arr[0])
    curr_node=head
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        curr_node.next=new_node
        new_node.prev=curr_node
        curr_node=curr_node.next
    return head

def remove_duplicates(head):
    seen = set()
    curr = head

    while curr:
        if curr.val in seen:
            # remove node
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        else:
            seen.add(curr.val)

        curr = curr.next

    return head

def remove_duplicates_optimal(head):
    curr_node=head
    while curr_node:
        if curr_node.prev:
            prev_value=curr_node.prev.val
            if prev_value==curr_node.val:
                if curr_node.prev==head:
                    curr_node.prev=None
                    head=curr_node
                else:
                    print(f'prev_value {prev_value}')
                    curr_node.prev.prev.next=curr_node
                    curr_node.prev=curr_node.prev.prev
        curr_node=curr_node.next

    return head



def main():
    arr=[1,1,2,2,2,3,3,4,5,6,6,6,7]
    head=ddl(arr)
    print(f'head {head}')
    # ans=remove_duplicates(head)
    ans=remove_duplicates_optimal(head)
    curr_node=ans
    while curr_node is not None:
        value=curr_node.val
        print(value,end=" ")
        curr_node=curr_node.next
    print()
    return ans

if __name__=="__main__":
    main()



        

