import operator

class BinSearchTree:
	def __init__(self, r=None):
		self.root = BinTreeNode(r)
		self.preorder = []
		self.postorder = []

	def insert(self, k, x):
		z = BinTreeNode()
		z.key = k
		z.left_child = None
		z.right_child = None
		y = x.parent
		while (x != None):
			y = x
			if (k < x.key):
				x = x.left_child
			else:
				x = x.right_child
		z.parent = y
		if (k < y.key):
			y.left_child = z
		else:
			y.right_child = z

	def search(self, k, x):
		if (x == None):
			return None
		elif (x.key == k):
			return x
		elif (k < x.key):
			return self.search(k, x.left_child)
		else:
			return self.search(k, x.right_child)

	def minimum(self, x):
		if (x == None):
			return None
		else:
			if x.left_child:
				return self.minimum(x.left_child)
			else:
				return x.key

	def maximum(self, x):
		if (x == None):
			return None
		else:
			if x.right_child:
				return self.maximum(x.right_child)
			else:
				return x.key

	def successor(self, x):
		if (x.right_child != None):
			return self.minimum(x.right_child)
		y = x.parent
		while (x != y.left_child) and (y != None):
			x = y
			y = y.parent
		return y

	def predecessor(self, x):
		if (x.left_child != None):
			return self.maximum(x.left_child)
		y = x.parent
		while (x != y.right_child) and (y != None):
			x = y
			y = y.parent
		return y

	def delete(self, x):
		if (x.left_child == None) and (x.right_child == None):
			if (x.parent.left_child == x):
				x.parent.left_child = None
			else:
				x.parent.right_child = None
		elif (x.left_child != None):
			if x.parent.left_child == x:
				x.parent.left_child = x.left_child
				x.left_child.parent = x.parent
			else:
				x.parent.right_child = x.left_child
				x.left_child.parent = x.parent
		elif (x.right_child != None):
			if x.parent.left_child == x:
				x.parent.left_child = x.right_child
				x.right_child.parent = x.parent
			else:
				x.parent.right_child = x.right_child
				x.right_child.parent = x.parent
		else:
			y = predecessor(x)
			x.key = y.key
			delete(y)

	def preorder_traversal(self, x):
		if x:
			self.preorder.append(x.key)
			self.preorder_traversal(x.left_child)
			self.preorder_traversal(x.right_child)

	def postorder_traversal(self, x):
		if x:
			self.postorder.insert(0, x.key)
			self.postorder_traversal(x.right_child)
			self.postorder_traversal(x.left_child)

	def printPostfix(self):
		self.postorder_traversal(self.root)
		print("Postfix: " + str(self.postorder))

	def printPrefix(self):
		self.preorder_traversal(self.root)
		print("Prefix: " + str(self.preorder))

class BinTreeNode:
	def __init__(self, k=None, p=None):
		self.parent = p
		self.left_child = None
		self.right_child = None
		self.key = k

def evaluate(node):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	leftChild = node.left_child
	rightChild = node.right_child
	if leftChild and rightChild:
		func = opers[node.key]
		return func(int(evaluate(leftChild)), int(evaluate(rightChild)))
	else:
		return int(node.key)

def buildParseTree(fpexp):
	fplist = fpexp.split()
	T = BinSearchTree()
	currentNode = T.root
	for i in fplist:
		if i == '(':
			currentNode.left_child = BinTreeNode(p=currentNode)
			currentNode = currentNode.left_child
		elif i not in ['+', '-', '*', '/', ')']:
			currentNode.key = i
			currentNode = currentNode.parent
		elif i in ['+', '-', '*', '/']:
			currentNode.key = i
			currentNode.right_child = BinTreeNode(p=currentNode)
			currentNode = currentNode.right_child
		elif i == ')':
			currentNode = currentNode.parent
		else:
			raise ValueError
	return T

def main():
	ex = "( ( 5 * ( ( 16 / 2 ) + 8 ) ) - 9 )"
	pt = buildParseTree(ex)
	print("Expression: " + ex)
	pt.printPostfix()
	pt.printPrefix()
	print("Answer: " + str(evaluate(pt.root)))

if __name__ == '__main__':
	main()
