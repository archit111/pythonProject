class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class queue:

    def __init__(self):
        self.head=self.tail=None

    def isEmpty(self):
        if self.head==None:
            return "the queue is empty"

    def peek(self):
        if self.head is None :
            return 0
        if self.head==self.tail:
            return self.tail.data
        return self.tail.data

    def push(self,new_data):
        new_node=Node(new_data)
        if self.tail is None:
            self.head=self.tail=new_node
            return
        self.tail.next=new_node
        self.tail=new_node

    def pop(self):

        if self.isEmpty():
            return
        self.head = self.head.next
        return self.head




if __name__=="__main__":

    q=queue()
    q.push(10)
    q.push(30)
    q.push(50)
    q.pop()
    print(q.peek())
    print("Queue Head " + str(q.head.data))
    print("Queue Tail " + str(q.tail.data))


