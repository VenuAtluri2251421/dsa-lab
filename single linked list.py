class node:
    def __init__(self,data):
              self.data=data
              self.nxt=None

class linkedlist:
    def __init__(self):
               self.head=None
    def printlist(self) :
            p=self.head
            print("data items of all are:")
            while(p):
                    print(p.data)
                    p=p.nxt
    def push(self,newdata):
            newnode=node(newdata)
            newnode.nxt=self.head
            self.head=newnode
    def pushatend(self,newdata):
            newnode=node(newdata)
            p=self.head
            if (p.nxt==None):
                    self.head=newnode
            while(p.nxt):
                p=p.nxt
            newnode.nxt=None
            p.nxt=newnode
	     
llist=linkedlist()
llist.head=node(10)
second=node(20)
third=node(30)
fourth=node(40)
llist.head.nxt=second
second.nxt=third
third.nxt=fourth
llist.printlist()
llist.push(5)
llist.printlist()
llist.pushatend(50)
llist.printlist()
