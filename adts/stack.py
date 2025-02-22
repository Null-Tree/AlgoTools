class Stack:
    def __init__(self):
        self.Stack=[]

    def push(self,val):
        self.Stack.append(val)
        
    def pop(self):
        lengh=len(self.Stack)
        if lengh==0:
            return None
        else:
            return self.Stack.pop(lengh-1)
        
    def top(self):
        lengh=len(self.Stack)
        if lengh==0:
            return None
        else:
            return self.Stack[lengh-1] 
        
    def isEmpty(self):
        return (True if len(self.Stack) == 0 else False)
    def print(self):
        print(self.Stack)
    

        

        
S=Stack()
S.push("a")
S.push("b")
S.pop()
S.push("c")
S.push("d")
print(S.Stack)