class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class circularll:



    def __init__(self):
        self.last=None

    def addbegin(self,new_data):
        new_node=Node(new_data)
        if self.last==None:
            return self.addtoempty(new_data)

        new_node.next=self.last.next
        self.last.next=new_node
        return self.last


    def addtoempty(self,new_data):
        new_node=Node(new_data)
        if(self.last!=None):
            return self.last
        self.last=new_node
        self.last.next=self.last
        return self.last

    def insert_node_at_last(self,new_data):
        new_node=Node(new_data)
        if(self.last==None):
            return self.addtoempty(new_data)
        new_node.next=self.last.next
        self.last.next=new_node
        self.last=new_node

    def addafter(self,item,new_item):
        new_node=Node(new_item)
        if (self.last==None):
            return self.addtoempty(new_item)

        temp=self.last.next
        while(temp):
            if (temp.data==item):
                new_node.next=temp.next
                temp.next=new_node

                if (temp==self.last):
                    self.last=new_node
                    return self.last
                else:
                    return self.last
            temp=temp.next
            if temp==self.last.next:
                #print ("element not present in  list")
                break




    def traverse(self):
        if(self.last==None):
            print ("empty circular linked list")
            return

        temp=self.last.next
        while (temp):
            print(temp.data)
            temp=temp.next
            if (temp==self.last.next):
                break

    def split(self):
        c=0
        if (self.last==None):
            print ("linkedlist cannot be splitted")
        temp=self.last.next
        while(temp):
            temp = temp.next
            c = c + 1
            if (temp==self.last.next):
                break
        print('First List')
        temp1 = self.last.next
        for i in range(0,c//2):
            print(temp1.data)
            temp1=temp1.next
        print('Second List')
        temp2=temp1
        for i in range(c//2-1,c-1):
            print(temp2.data)
            temp2=temp2.next

    def sorted_insert(self,new_data):
        new_node=Node(new_data)
        temp=self.last.next
        if (new_node.data > temp.data):
            temp = temp.next
        new_node.next=temp.next
        temp.next=new_node

                #new_node.next = temp



        '''new_node = Node(new_data)
            # Locate the node before the point of insertion
        current = self.last
        while (current.next is not None and
                current.next.data < new_node.data):
            current = current.next

        new_node.next = current.next
        current.next = new_node'''
    def removeloop(self,l):
        temp=self.last.next
        c=1
        while(temp):
            if l==1:
                self.last.next=None
                print("The linked list do not contain any loop")
                break
            c=c+1
            if c==l:
                temp.next=None

            temp=temp.next

            if temp==self.last.next:
                break



if __name__ == '__main__':

    cir=circularll()
    last=cir.addtoempty(2)
    cir.addafter(2,5)
    #cir.addbegin(7)
    cir.addafter(5,7)
    cir.addafter(7,9)
    cir.addafter(9,10)
    '''cir.insert_node_at_last(10)
    cir.insert_node_at_last(15)
    cir.insert_node_at_last(19)
    cir.addbegin(25)'''
    #cir.split()
    cir.sorted_insert(6)
    #cir.removeloop(1)
    cir.traverse()
