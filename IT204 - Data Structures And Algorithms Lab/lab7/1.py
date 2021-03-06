import math

class BinaryHeap:
	def __init__(self, arr):
		self.heapArray = arr
		self.build_heap()

	def insert(self, k):
		self.heapArray.append(k)
		index = len(self.heapArray) - 1
		if (index % 2):
			parent = int(index / 2)
		else:
			parent = int(math.floor(index / 2) - 1)
		while True:
			if (parent >= 0) and (self.heapArray[index] > self.heapArray[parent]):
				self.heapArray[index], self.heapArray[parent] = self.heapArray[parent], self.heapArray[index]
			else:
				break
			index = parent
			if (index % 2):
				parent = int(index / 2)
			else:
				parent = int(math.floor(index / 2) - 1)

	def maximum(self):
		return self.heapArray[0]

	def heapify(self, i):
		index = i
		leftChild = index * 2 + 1
		rightChild = leftChild + 1
		leftChildExists = False
		rightChildExists = False
		if leftChild < len(self.heapArray):
			leftChildExists = True
		if rightChild < len(self.heapArray):
			rightChildExists = True
		while True:
			if leftChildExists and rightChildExists and (self.heapArray[index] < self.heapArray[leftChild]) and (self.heapArray[index] < self.heapArray[rightChild]):
				if self.heapArray[leftChild] > self.heapArray[rightChild]:
					child = leftChild
				else:
					child = rightChild
			elif leftChildExists and (self.heapArray[index] < self.heapArray[leftChild]):
				child = leftChild
			elif rightChildExists and (self.heapArray[index] < self.heapArray[rightChild]):
				child = rightChild
			else:
				break
			self.heapArray[index], self.heapArray[child] = self.heapArray[child], self.heapArray[index]
			index = child
			leftChild = index * 2 + 1
			rightChild = leftChild + 1
			leftChildExists = False
			rightChildExists = False
			if leftChild < len(self.heapArray):
				leftChildExists = True
			if rightChild < len(self.heapArray):
				rightChildExists = True

	def build_heap(self):
		lastIndex = len(self.heapArray) - 1
		if (lastIndex % 2):
			index = int(lastIndex / 2)
		else:
			index = int(math.floor(lastIndex / 2) - 1)
		while index >= 0:
			self.heapify(index)
			index -= 1

	def extract_max(self):
		toret = self.heapArray[0]
		self.heapArray[0] = self.heapArray.pop(-1)
		self.heapify(0)
		return toret

	def __str__(self):
		return str(self.heapArray)

def main():
	H = BinaryHeap([10, 15, 30, 40, 50, 100, 5])
	print(H)
	print(H.extract_max())
	print(H)
	print(H.maximum())

if __name__ == '__main__':
	main()