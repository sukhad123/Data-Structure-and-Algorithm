class Queue:
    def __init__(self, length):
        self.length = length
        self.list = [None] * self.length
        self.front = 0
        self.back = 0
        self.used = 0
     
    def haveSpace(self):
        if self.used < self.length:
            return True
        return False   
    def push_back(self, data):
        
        if self.back == self.length and self.used < self.length:
            self.back = self.capacity % self.back
            self.back -= 1
        else:
            self.list[self.back] = data
            self.back += 1
        #regular adding of the data
              
        self.used += 1
        
    #removing the data from the back
    def pop_back(self):
        self.list[self.back] = None
        self.back -= 1
        self.used -= 1
    
    def push_front(self, data):
        if self.front != 0:
            self.list[self.front] = data
            self.front += 1
            
        else:
            self.front = self.length -1
            self.list[self.front] = data
            self.front -= 1
        self.used -= 1
            
        
            
    def pop_front(self):
        self.list[self.front] = None
        self.front -= 1
        self.used -= 1
        
        
    def printing(self):
        for i in range(self.length):
            print(self.list[i])
#defining the queueu
data = Queue(5)
data.push_front(3)
data.printing()
data.push_back(4)
data.printing()
data.pop_back()
data.printing()