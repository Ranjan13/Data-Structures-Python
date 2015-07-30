class Stack:
	def __init__(self,limit = 10):
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
		if (len(self.stk) <= 0):
			print "Stack Underflow"
			return 0
		else:
			self.stk.pop()
	def size(self):
		return len(self.stk)
	def printStack(self):
		if(len(self.stk) <= 0):
			print "Yay!!, Underflow"
			return 0
		else:
			for i in range(1,(len(self.stk))+1):
				print self.stk[-i]
st = Stack(5)
st.StackPush("2")
st.StackPush("1")
st.StackPush("12")
print st.printStack()
