class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.count=0
    def dequeue(self):
        if self.front is None:
            print('Queue Under Flow')
            exit(-1)
        temp=self.front
        print('deletin',temp.data)

        self.front=self.front.next
        if self.front is None:
             self.rear=None
        self.count-=1
        return temp.data
    def enqueue(self,item):
        node=Node(item)
        print('adding',item)

        if self.front is None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.count+=1
    def peek(self):
        if self.front:
            return self.front.data
        else:
            exit(-1)
    def isempty(self):
        return self.rear is None and self.front is None
    def size(self):
        return self.count
if __name__=='__main__':
 qu=Queue()
 qu.enqueue(1)
 qu.dequeue()
