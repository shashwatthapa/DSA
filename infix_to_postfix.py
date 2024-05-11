class Stack:
    def __init__(self,top,size):
        self.size = size
        self.top = top
        self.array = [None]*size
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
        self.top = self.top +1
        self.array[self.top] = x
    def pop(self):
        self.top = self.top-1
    def peek(self):
        return self.array[self.top]
def precedance(character):
    if (character=='^'):
        return 3
    elif (character=='*' or character=='/'):
        return 2
    elif (character=='+' or character=='-'):
        return 1
    else:
        return -1
s1 = Stack(-1,5)
def infix_to_postfix(expression):
    for ch in expression:
        if (ch.isalnum()):
            print(ch,end="")
        else:
            if (ch=='('):
                s1.push(ch)
            elif s1.isEmpty():
                s1.push(ch)
            elif (ch==')'):
                while (s1.peek()!='('):
                    print(s1.peek(),end="")
                    s1.pop()
                s1.pop()
            else:
                if (precedance(ch)>precedance(s1.peek())):
                    s1.push(ch)
                else:
                    while (not s1.isEmpty() and precedance(ch)<=precedance(s1.peek())):
                        print(ch,end="")
                        s1.pop()
    while (not s1.isEmpty()):
        print(s1.peek(),end="")
        s1.pop()
a = input("Enter the expression: ")
infix_to_postfix(a)


