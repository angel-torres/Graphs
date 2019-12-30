class Stack:
	def __init__(self, size):
		self.stack = [0] * size

	def push(self, value):
		self.stack[len(self.stack) - 1] = value


s = Stack(8)
s.push(4)
s.push(5)

print(s.stack)

