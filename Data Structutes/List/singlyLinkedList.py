#SinglyLinkedList have a data and next pointer pointing to the next element
class SinglyLinkedList:
    #Implementation of Node inside the list
    class Node:
        def __init__(self, data =None, next = None):
            self.data = data
            self.next = next
    def __init__(self):
        self.front = None
        self.back = None
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
    def push(self,data):
        if (self.isEmpty()):
            Node = self.Node(data)
            self.front = Node
            self.back = None
         
        else:
            Node = self.Node(data,self.front )
            self.front = Node
           
   
   
#implementation Example
list = SinglyLinkedList()
list.push(4)
print(list.isEmpty())