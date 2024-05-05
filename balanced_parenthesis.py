import sys
class Stack:
    def __init__(self,top,size):
        self.top = top
        self.size = size
        self.stack = [None] * size
    def isEmpty(self):
        if (self.top==-1):
            return True
        else:
            return False
    def isFull(self):
        if (self.top==self.size-1):
            return True
        else:
            return False
    def push(self,ch):
        self.top = self.top+1
        self.stack[self.top] = ch
    def pop(self):
        self.top = self.top-1
    def peek(self):
        return self.stack[self.top]
s1 = Stack(-1,10)
def matching(bracket1,bracket2):
    if (bracket1=='(' and bracket2==')'):
        return True
    elif (bracket1=='{' and bracket2=='}'):
        return True
    elif (bracket1=='[' and bracket2==']'):
        return True
    else:
        return False
a = list(input("Enter brackets: "))
for i in a:
    if (i=='(' or i=='{' or i=='['):
        s1.push(i)
    else:
        if (matching(s1.peek(),i)):
            s1.pop()
        else:
            print("Unbalanced parenthesis\n")
            sys.exit()
if (s1.isEmpty()):
    print("Balanced parenthesis")
else:
    print("Unbalanced parenthesis")