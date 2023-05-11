class node:
       def __init__(self,data):
           self.item=data
           self.next=None
           self.prev=None

class doublylinkedlist:
       def __init__(self):
            self.head=None
       def inserttoemptylist(self,data):
              if self.head is None:
                  newnode=node(data)
                  self.head=newnode
              else:
                  print("the list is empty")
       def inserttoend(self,data):
               if self.head is None:
                   newnode=node(data)
                   self.head=newnode
                   return
               n=self.head
               while n.next is not None:
                        n=n.next
               newnode=node(data)
               n.next=newnode
               newnode.prev=n
       def deleteatstart(self):
                if self.head is None:
                       print("the linked list is empty nothing to delete")
                       return
                if self.head.next is None:
                     self.head=None
                     return
                self.head=self.head.next
                self.start_prev=None;
       def deleteatend(self):
                 if self.head is None:
                     print("list is empty nothing to delete")
                     return
                 if self.head.next is None:
                      self.head=None
                      return
                 n=self.head
                 while n.next is not None:
                     n=n.next
                 n.prev.next=None
       def display(self):
                  if self.head is None:
                      print("the list is empty")
                      return
                  else:
                      n=self.head
                      while n is not None:
                          print("element is",n.item)
                          n=n.next
                          




newdoublylinkedlist=doublylinkedlist()
newdoublylinkedlist.inserttoemptylist(10)
newdoublylinkedlist.inserttoend(20)
newdoublylinkedlist.inserttoend(30)
newdoublylinkedlist.inserttoend(40)
newdoublylinkedlist.inserttoend(50)
newdoublylinkedlist.inserttoend(60)
newdoublylinkedlist.display()
print("\nnew list after deleting first and last element\n")
newdoublylinkedlist.deleteatstart()
newdoublylinkedlist.deleteatend()
newdoublylinkedlist.display()

         
