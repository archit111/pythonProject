class Node:
    def __init__(self, data):
        self.next=None
        self.prev=None
        self.data=data


class DoublyLinkedList:

    def __int__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)

        new_node.next=self.head
        new_node.prev=None
        self.head.prev=new_node
        self.head=new_node

    def insertafter(self,prev_node,new_data):

        if prev_node is None:
            print ("the given previous node cannot be null")
            return
        new_node=Node(new_data)
        #temp=self.head
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def append (self,new_data):
        temp=self.head
        new_node=Node(new_data)
        while(temp.next!=None):
            temp = temp.next
        temp.next=new_node
        new_node.prev = temp
        return


    def delete(self,prev_node,node,next_node):
        temp=self.head
        while(temp is None and temp.data!=node):
            temp=temp.next
        if (temp!=None):
            prev_node.next=node.next
            next_node.prev=prev_node

    def delete1(self,node):
        if self.head==node:
            self.head=node.next
        node.prev.next=node.next

    def delete_at_nth_position(self,n):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        temp=self.head
        for i in range (1,c+1):
            if (i==n):
                temp.prev.next=temp.next
                break
            temp=temp.next








    def print (self):

        print('printing in reverse direction')
        temp = None
        current = self.head

        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev
        #last=None
        c=0
        temp=self.head
        while(temp):
            c=c+1
            print(temp.data)
            temp=temp.next


    #print("Total number of nodes in a doubly linked list is",c)
    def duplicate(self):
        temp = self.head

        while(temp):
            temp1 = temp.next
            while (temp1):
                if (temp.data == temp1.data):
                    temp1.prev.next = temp1.next
                temp1 = temp1.next
            temp=temp.next

    def removealloccurences(self,key):
        temp=self.head
        temp1=temp.next
        while(temp1):
            if temp==key:
                temp1.prev=temp.prev

            if temp1.data==key:
                temp1.prev.next=temp1.next
            temp1=temp1.next
        print ("There is no such element in a a list")


if __name__=='__main__':

    dd=DoublyLinkedList()
    dd.head=Node(2)
    second=Node(5)
    third=Node(6)
    fourth=Node(3)

    dd.head.prev=None
    dd.head.next=second
    second.prev = dd.head
    second.next=third
    third.prev = second
    third.next=fourth
    fourth.prev=third
    fourth.next=None

    dd.push(7)
    dd.push(10)
    dd.insertafter(dd.head,12)
    #dd.append(23)
    #dd.append(24)
    #dd.delete(dd.head.next,dd.head.next.next,dd.head.next.next.next)
    #dd.delete1(dd.head.next)
    #dd.delete_at_nth_position(2)
    #dd.duplicate()
    #dd.removealloccurences(10)
    #dd.print()
    dd.swappairs()




