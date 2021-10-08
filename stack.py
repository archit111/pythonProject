class stacknode:

    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.root=None

    def isEmpty(self):
        if self.root is None:
            return True

    def push(self,new_data):
        #temp=self.root
        new_node=stacknode(new_data)
        new_node.next=self.root
        self.root=new_node
        print ("data pushed to stack")


    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp=self.root
        self.root=self.root.next
        popped=temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

    def print(self):
        temp=self.root
        while(temp):
            print(temp.data)
            temp=temp.next

    def getmin(self,new_data):
        new_node = stacknode(new_data)
        ms.push





stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(50)
stack.pop()
stack.pop()
ms=[]
aus=[]
print(stack.peek(),'a')
stack.print()