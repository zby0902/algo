from queue import Queue
class myQueue:
    def __init__(self):
        self.items = Queue()
    def enque(self,x):
        self.items.put(x)
    def deque(self):
        return self.items.get()
