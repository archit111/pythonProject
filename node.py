class Node:

    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertafter(self, prev_node, new_data):

        if prev_node is None :
            print ("error")
        new_node=Node(new_data)   # create new node and put in the data
        new_node.next=prev_node.next
        prev_node.next=new_node

    def insertBefore (self,prev_node,next_node, new_data):

        if next_node is None :
            print ("error")
        new_node=Node(new_data)
        new_node.next=next_node.next

        prev_node.next=new_node
        new_node.next = next_node

    def delete (self,prev_node,next_node,node):

            if prev_node.data==next_node.data:
                prev_node.next =next_node.next








    def append(self, new_data):

        new_node= Node(new_data)   # creating a new node and inserting a data

        if self.head is None :
            self.head =new_node
            return

        last=self.head
        while(last.next):
            last=last.next

        last.next =new_node

    def printList(self):

        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next


if __name__ == '__main__':
    lis=Linkedlist()

    lis.append(6)
    lis.push(4)
    lis.push(7)
    lis.append(1)

    #lis.insertafter(lis.head,8)

    #lis.insertBefore(lis.head.next,lis.head.next.next,9)
    lis.delete(lis.head,lis.head.next.next,lis.head.next)
    print ('Linked list is ')

    lis.printList()
