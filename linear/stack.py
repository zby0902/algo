class Stack:
    """
    A linear abstract data type that follow the rule of LIFO(last in first out)
    """
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item) 
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items) 

