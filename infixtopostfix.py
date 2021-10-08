class stacknode():
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.root=None

    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.output=[]
        self.array=[]
        self.precedence={'+':1, '-':1, '*':2, '/':2, '^':3}


    '''def push (self,new_data):
        new_node=stacknode(new_data)
        temp=self.root
        new_node.next=self.root
        self.root=new_node
        print("data pushed to stack")'''
    def push(self,op):
         self.top=self.top+1
         self.array.append(op)

    '''def pop(self):
        temp = self.root
        if self.isEmpty():
            return float("-inf")

        self.root=self.root.next
        popped=temp.data
        return popped'''
    def pop(self):
        if (not self.isEmpty()):
            self.top=self.top-1
            self.array.pop()
        else:
            return '$'



    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False


    def peek(self):
        return self.array[-1]

    def print(self):
        temp=self.root
        while(temp):
            print(temp.data)
            temp=temp.next


    def isOperand(self,ch):
        return ch.isalpha()

    def notGreater(self,i):
        a=self.precedence[i]
        b=self.precedence[self.peek()]
        try:
            if a<=b:
                return True
            else:
                return False
        except KeyError:
            return False


    def infixtopostfix(self,exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)

            elif i=='(':
                self.push(i)

            elif(i==')'):
                while((not self.isEmpty()) and self,peek!='('):
                    a=self.pop()
                    self.output.append(a)
                    if (not self.isEmpty()  and self.peek!='('):
                        return -1
                    else:
                        self.pop()

            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while (not self.isEmpty()):
            self.output.append(self.pop())

        print ("".join(self.output()))


exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Stack(len(exp))
obj.infixtopostfix(exp)


'''stack=Stack()
stack.push(30)
stack.push(15)
#stack.pop()
stack.print()
print(stack.peek(),'a')'''


