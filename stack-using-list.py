class Stack:
        def __init__(self,limit = 1000):
                self.stk = list()
                self.limit = limit
        def isEmpty(self):
                return len(self.stk <= 0)
        def StackPush(self,item):
                if (len(self.stk) >= self.limit):
                        print "Stack Overflow"
                        return 0
                else:
                        self.stk.append(item)
        def StackPop(self):
                if (len(stack.stk) <= 0):
                        print "Stack Underflow"
                        return 0
                else:
                        self.stk.pop()
        def size(self):
                return len(self.stk)
        def printStack(self):
                if(len(self.stk) <= 0):
                        print "Underflow"
                        return 0
                else:
                        self.stk[-1]
st = Stack(100)
print st.printStack()
st.StackPush("2")
st.StackPush("1")
st.StackPush("12")
print st.printStack()
