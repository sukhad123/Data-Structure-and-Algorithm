class Stack:
    def __init__(self, length):
        self.list = [None] * length
        self.length = length
        self.data_list = 0
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def push(self,data):
        #if our stack have some data
        if self.data_list < self.length:
            #find the empty space and store the data
            self.list[self.data_list]  = data;
            #increase the value of the data list in the list
            self.data_list += 1
    #removing the last data
    def pop(self):
        print("Removing Value")
        print(self.list[self.data_list -1])
        self.list[self.data_list -1] = None
        self.data_list -= 1
    
    def printing(self):
        print("Data in the list:")
        for i in range(0,self.data_list):
            print(self.list[i]) 
            
firstStack = Stack(5);
firstStack.push(1)
firstStack.printing()
firstStack.push(2)
firstStack.push(3)
firstStack.printing()
firstStack.pop()
firstStack.printing()
 

