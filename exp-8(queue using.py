class queue:
        def __init__(self,c):
             self.queue=[ ]
             self.front=self.rear=0
             self.capacity=c
        def queueEnqueue(self,data):
             if(self.capacity==self.rear):
                    print("\nQueue is full")
             else:
                    self.queue.append(data)
                    self.rear +=1
        def queueDisplay(self):
             if(self.front==self.rear):
                    print("\nQueue is empty")
             for i in self.queue:
                    print(i,"<--",end='')
        def queueFront(self):
             if(self.front==self.rear):
                    print("\nQueue is empty")
             else:
                    print("\nfront element is:-",self.queue[self.front])
if __name__=='__main__':
        q=queue(4)
        q.queueEnqueue(20)
        q.queueEnqueue(30)
        q.queueEnqueue(50)
        q.queueDisplay()
        q.queueEnqueue(60)
        q.queueDisplay()
        q.queueFront()
                 
