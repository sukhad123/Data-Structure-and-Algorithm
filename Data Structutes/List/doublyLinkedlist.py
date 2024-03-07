
#Doubly LinkedList contains a node of data, a pointer pointing to the next element and another pointer pointing to the previous element

class DoublyLinkedList:
    class Node:
        def __init__(self, data, next, prev):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self):
        self.front = None
        self.back = None
    
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
    def push(self,data):
        Node = self.Node(data, None, None)
        if self.isEmpty():
            
            #Both front and back pointing to that node
            self.front = Node
            self.back = Node
        else:
            Node.next = self.front.next
            self.front.prev = Node
            self.front.next = Node
            Node.prev = self.front
            
    def pop(self):
        #access the last element
        nodeToRemove = self.back.next 
        self.back.next = nodeToRemove.prev
        nodeToRemove.prev.next = None
        nodeToRemove = None
            
    def print(self):
        if self.isEmpty():
            print("There is nothing in this list")
            return
        else:
            current_node = self.front
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

#Implementation Example of Doubly Linked list
lst = DoublyLinkedList()
lst.push(5)
lst.push(6)
lst.pop()
lst.print()