# node class to create  a single node
import math
class Node:
    def __init__(self, data ):
        self.data=data
        self.next=None

class  LinkedList:
    def __init__(self):
        self.head=None


    def display(self):
        temp=self.head
        c=0
        while (temp):
            c=c+1                  # to count the number of nodes traversed
            print(temp.data)
            prev=temp
            temp=temp.next
        print ('Number of nodes in a link list ')
        print (c)

    def push(self,new_data):  #to insert an element in front of a list

        new_node=Node(new_data)
        #if self.head != None:
        new_node.next=self.head
        self.head=new_node

    def append (self,new_data):  # to insert an element at the end
        new_node=Node(new_data)
        temp=self.head
        while (temp.next):
            temp=temp.next
        temp.next=new_node


    def insertafter(self,prev_node,new_data):
        new_node=Node(new_data)
        new_node.next = prev_node.next
        prev_node.next=new_node


    def insertbefore(self,new_data,next_node,prev_node):  # inserting before an element

        new_node=Node(new_data)
        if next_node == self.head:
            self.head=new_node
            #new_data.next=self.head
        else:
            new_node.next=prev_node.next
            prev_node.next=new_node
            new_node.next=next_node

    def delete (self,val):
        temp=self.head
        if temp is not None :
            if temp.data==val:
                self.head=temp.next
        while (temp is not None ):
            if temp.data==val:
                break
            prev=temp
            temp=temp.next
            prev.next=temp.next
            temp=None

    def deletelinkedlist(self):
        self.head=None

    def search(self,val):
        temp=self.head
        c=0
        while(temp):
             c=c+1
             if (temp.data==val):
                print("value present in linked list at position")
                print (c)
                return

             temp=temp.next
        print ('value not present in linked list')

    def get_node_at_nth_position(self,n):
        temp=self.head
        c=0
        while (temp):
            c=c+1
            if (c==n):
                print(temp.data)
                return
            temp=temp.next
        if (c<n):
            print ('element not present in range ')
            
    def get_node_at_nth_position_last(self,n):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        temp1=self.head
        k=c-n
        for i in range(c,0,-1):
            if i==k+1:
                print(temp1.data)
            temp1=temp1.next

                

    def reverse(self):    # to reverse the linkedlist
        prev=None
        current=self.head
        while(current is not None ):
            next = current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def node_at_tail(self,new_data):
        new_node=Node(new_data)
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=new_node

    def middle_element(self):
        c=0
        temp=self.head
        while(temp):
            c=c+1
            temp=temp.next
        temp = self.head
        for i in range (0,c//2):
            temp=temp.next
        print(temp.data)

    def circular(self):
        temp=self.head
        node=temp.next
        while ( node !=temp):
            node=node.next
            if (temp==node):
                print('a')
                break
        print ("not a circular linked list ")

    def insertnodeinmiddle(self,new_data):
        new_node=Node(new_data)
        temp=self.head
        c=0
        while(temp):
           c=c+1
           temp=temp.next
        temp = self.head
        for i in range (0,c):
            if (i==c//2-1):
                new_node.next=temp.next
                temp.next=new_node
            temp=temp.next

    def add (self,new_data1,new_data2):
        c=0
        new_node1=Node(new_data1)
        new_node2=Node(new_data2)
        self.head=new_node1
        new_node1.next=new_node2
        new_node2.next=None
        temp=self.head
        while(temp is not None ):
            c=c+temp.data
            temp=temp.next
        print (c)

    def swappairs(self):
        temp=self.head
        while(temp is not None and temp.next is not None):
            if temp.data==temp.next.data:
                temp=temp.next.next
            else:
                temp.data,temp.next.data=temp.next.data,temp.data
                temp=temp.next.next

        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def pallindrome (self):
        ispalin=True
        stack=[]
        temp=self.head
        while (temp):
            stack.append(temp.data)
            temp=temp.next

        slow=self.head
        while(slow):
            i=stack.pop()
            if i==slow.data:
                ispalin=True
            else:
                ispalin=False
                break
            slow=slow.next

        return ispalin

    def isLoopinLinkedList(self,fast_p,slow_p):
        fast_p=self.head
        slow_p=self.head

        while (fast_p!=None and fast_p.next!=None):
            fast_p=fast_p.next.next
            slow_p=slow_p.next
            if (fast_p==slow_p):
                return True
        return False

    def removenodeofgivenreference (self,node):
        temp=self.head
        curr=Node(node)
        while (temp):
            if temp.data==curr.data:
                temp.data=temp.next.data
                temp.next=temp.next.next
                break
            temp=temp.next
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def fractionalnode (self,K):
        temp=self.head
        c=0
        while (temp):
            c=c+1
            temp=temp.next
        x=math.ceil(c/K)
        temp1=self.head
        c=0
        while (temp1):
            c = c + 1
            if c==x:
                return temp1.data

            temp1=temp1.next




# code execution starts here
if __name__=='__main__':

    lis=LinkedList()
    lis.head=Node(1)  # create a node with element 1
    second =Node(2)    # create a node with element 2
    third=Node(4)
    fourth=Node(7)
    fifth=Node(9)
    sixth=Node(10)
    '''lis = LinkedList()
    lis.head = Node('R')  # create a node with element 1
    second = Node('A')  # create a node with element 2
    third = Node('D')
    fourth = Node('A')
    fifth = Node('R')'''



    lis.head.next=second   # used to link a head or the first node with the second
    second.next=third      # used to link a second node with the other node
    third.next=fourth
    fourth.next=fifth
    fifth.next=sixth


    #lis.display()
    #lis.push(2)
    #lis.append(12)
    #lis.insertafter(lis.head.next.next,15)
    #lis.insertbefore(21,lis.head.next.next.next,lis.head.next.next)
    #lis.delete(2)
    #lis.deletelinkedlist()
    #lis.reverse()
    #lis.circular()
    #lis.node_at_tail(56)
    #lis.node_at_tail(58)
    #lis.insertnodeinmiddle(6)
    #lis.display()
    #lis.middle_element()
    #lis.get_node_at_nth_position_last(4)
    #lis.search(9)
    #lis.get_node_at_nth_position(3)
    #lis.add(8,14)
    #lis.swappairs()
    #lis.pallindrome())
    #print(lis.isLoopinLinkedList(1,1))
    #lis.removenodeofgivenreference(9)
    #lis.swapnopdes()
    print (lis.fractionalnode(1))