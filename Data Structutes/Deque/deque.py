class Deque:
    def __init__(self, length):
        self.list = [None] * length
        self.length = length
        self.data_list = 0
        self.front = 0
        self.back = 0
    
    def isEmpty(self):
        if self.data_list == 0:
            return True
        else:
            return False
    
    def push(self,data):
        #if our stack have some data
        
        #if the array is full and there is some vacant space in the front
        #linear Probing
        if self.back == self.length and self.front > 0:
            self.back = self.back % self.length
            self.front -= 1
        if self.data_list < self.length:
            #find the empty space and store the data
            self.list[self.back]  = data;
            #increase the value of the data list in the list
            self.data_list += 1
            self.back += 1
    #removing the last data
    def pop(self):
        print("Removing Value")
        print(self.list[self.front])
        self.list[self.front] = None
        self.data_list -= 1
        self.front += 1
    
    def printing(self):
        print("Data in the list:")
        for i in range(0, self.length):
            print(self.list[i])
            
 
 

data = Deque(2)
data.push(1)
data.push(2)
 
data.printing()
data.pop()
data.printing()
data.push(3)
data.printing()
