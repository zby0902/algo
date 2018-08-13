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


def baseConverter(number,base):
    """
    A base converter method based on the stack class
    """
    if base > 16:
        raise ValueError('The limit of base is hex or 16')
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    while number > 0:
        rem = number % base
        rem_stack.push(rem)
        number = number//base
    num_string = ''
    while not rem_stack.isEmpty():
        num_string += str(digits[rem_stack.pop()])
    return num_string

def parChecker(symbolString):
    """
    A simple method checking the parentisises are balanced or not using stack
    """
   s = Stack() 
   balanced = True
   index = 0
   while index < len(symbolString) and balanced:
       symbol = symbolString[index]
       if symbol in '([{':
           s.push(symbol)
        else:
            top = s.top()
            if not matcheds(top,symbol):
                balanced =  False
        index += 1
    if balanced  and s.isEmpty():
        return True
    else:
        return False
def matches(openP,closeP):
    opens = '([{'
    closes = ')]}'
    return opens.index(openP) == closes.index(closeP)
