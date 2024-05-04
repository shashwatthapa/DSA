class Stack:
    def __init__(self,top,size):
        self.size = size;
        self.top = -1;
        self.array = [None] * size
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
        if (self.isFull()):
            print("Stack is full\n")
        else:
            self.top = self.top+1
            self.array[self.top] = x;
    def pop(self):
        if (self.isEmpty()):
            print("Stack is empty\n")
        else:
            print(f"{self.array[self.top]} has been popped\n")
            self.top = self.top-1;
    def peek(self):
        if (self.isEmpty()):
            print("Stack is empty\n")
        else:
            print(f"{self.array[self.top]} is at top of the array")

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.array[i])

s1 = Stack(-1,5)
run = True
while run:
    choice = int(input("Enter 1 to push, 2 to pop, 3 to peek, 4 to display and 5 to exit: "))
    if (choice==1):
        value = int(input("Enter a value to push: "))
        s1.push(value)
    elif (choice ==2):
        s1.pop()
    elif (choice==3):
        s1.peek()
    elif (choice ==4):
        s1.display()
    elif (choice==5):
        run = False
    else:
        print("Invalid....Try again\n")

