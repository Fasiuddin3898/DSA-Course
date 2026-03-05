#In this code we find the length of loop in linked list

#Brute force
def lenght_loop(head):
    travel=0
    dit={}
    temp=head
    while temp is not None:
        if temp in dit:
            print(f'length of a loop is {travel-dit[temp]}')
            return travel-dit[temp]
        dit[temp]=travel
        travel+=1
        temp=temp.next
    return None #loop is not involved in linked list


#optimal solution
def optimal(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=slow.next
            count=1
            while slow!=fast:
                slow=slow.next
                count+=1
            print(f'length of a loop is {count}')
            return count
    return None

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def create_linked_list(arr):
    if not arr:
        return None
    head=Node(arr[0])
    temp=head     #temp and head are pointing to the SAME object.
                  #They are NOT copies. They are two references to the same object.
    nodes=[head]
    for array in arr[1:]:
        new_node=Node(array)
        temp.next=new_node
        temp=new_node
        nodes.append(new_node)
    return head,nodes


def main():
    arr = [1, 2, 3, 4, 5]
    head,nodes=create_linked_list(arr)
    # Create loop (last node connects to node with value 3)
    nodes[-1].next=nodes[2]
    print("Brute Force Loop Length:", lenght_loop(head))
    print("Optimal Loop Length:", optimal(head))

if __name__=="__main__":
    main()



