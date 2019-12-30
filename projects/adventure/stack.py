class Node:
	def __init__(self, value=None):
		self.next = None
		self.value = value

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def addToHead(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node
		self.size += 1

	def removeFromHead(self):
		if self.size == 0:
			raise ValueError('There are no more nodes!')
		new_head = self.head.next
		self.head = new_head
		self.size -= 1

class Stack:
	def __init__(self, size):
		self.stack = [0] * size

	def push(self, value):
		for i in range(1, len(self.stack), 1):
			self.stack[i - 1] = self.stack[i]
		self.stack[len(self.stack) - 1] = value

	def pop(self):
		popped = self.stack[len(self.stack) - 1]
		for i in range(len(self.stack) - 2, -1, -1):
			self.stack[i + 1] = self.stack[i]
		return popped

