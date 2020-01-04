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
			return None
		new_head = self.head.next
		old_head = self.head
		self.head = new_head
		self.size -= 1
		return old_head 

class Stack:
	def __init__(self):
		self.stack = LinkedList()
		self.size = 0

	def push(self, value):
		self.stack.addToHead(value)
		self.size += 1

	def pop(self):
		self.size -= 1
		return self.stack.removeFromHead()

	def peek(self):
		if self.stack.head == None:
			return None

		return self.stack.head.value



