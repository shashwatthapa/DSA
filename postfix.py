class Stack:
    def __init__(self,top,size):
        self.top = top
        self.size = size
        self.stack = [None]*size
    def isFull(self):
        if (self.top==self.size-1):
            return True
        else:
            return False
    def isEmpty(self):
        if (self.top==-1):
            return True
        else:
            return False
    def push(self,x):
        if not self.isFull():
            self.top+=1
            self.stack[self.top] = x
    def pop(self):
        if not self.isEmpty():
            self.top-=1
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
def postfix(expression):
    result = 0
    s1 = Stack(-1,10)
    for i in expression:
        if (i.isalnum()):
            s1.push(i)
        else:
            operand1 = s1.peek()
            s1.pop()
            operand2 = s1.peek()
            s1.pop()
            expression = '{} {} {}'.format(operand1,i,operand2)
            result = eval(expression)
            s1.push(result)
    return s1.peek()
value = input("Enter the infix expression: ")
print(postfix(value))

