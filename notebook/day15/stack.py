class Stack(list):
    push = list.append
    
    def is_empty(self):
        if not len(self):
            return True
        else:
            return False
        
    def peek(self):
        return self[-1]
    
    def size(self):
        return len(self)