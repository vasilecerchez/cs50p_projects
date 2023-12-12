








class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError()
        self._capacity=capacity
        self._size=0
         

    def __str__(self):
            return "🍪"*self.size
            
    def deposit(self, n):
        if self.size+int(n)<=self.capacity:
            self._size=self.size+int(n)
        else:
            raise ValueError("Exceed capacity")
        

    def withdraw(self, n):
        if self.size-int(n)>=0:
            self._size=self.size-int(n)
        else:
            raise ValueError("Exceed capacity")

    @property
    def capacity(self):
        return self._capacity
    #@capacity.setter
    #def capacity(self, capacity):
    #    if capacity<0:
    #        raise ValueError()
    #    self._capacity=capacity
     
    
    
    @property
    def size(self):
        return self._size
    
        
    