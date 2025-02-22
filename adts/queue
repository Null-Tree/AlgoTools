from queue import Queue


class Queue:
    def __init__(self,maxsize:int):
        self.queue=[]
        self.maxsize=maxsize

    def qsize(self):
        return len(self.queue)
    
    def full(self):
        return (len(self.queue) == self.maxsize)
        
    def empty(self):
        return (len(self.queue)==0)
        
    def put(self,val):
        if len(self.queue)<self.maxsize:
            self.queue.append(val)
            return True
        else:
            return False
        
    def get(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            return None
    def print(self):
            print(self.queue)

        





queue = Queue(maxsize = 3)

# Get the current queue size
queue.qsize() # 0

# Enqueuing
queue.put('a')
queue.put('b')
queue.put('c')
print(queue.full())  # True

# Dequeuing
print(queue.get()) # a
print(queue.get()) # b
print(queue.get()) # c

queue.empty() # True

queue.put(1)
queue.empty() # False
queue.full() # False