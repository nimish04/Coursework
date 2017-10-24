import math

class BinaryHeap:
	def __init__(self, arr=[]):
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

	def heapify(self, i, maxIn):
		index = i
		leftChild = index * 2 + 1
		rightChild = leftChild + 1
		leftChildExists = False
		rightChildExists = False
		if leftChild < maxIn:
			leftChildExists = True
		if rightChild < maxIn:
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
			if leftChild < maxIn:
				leftChildExists = True
			if rightChild < maxIn:
				rightChildExists = True

	def build_heap(self):
		lastIndex = len(self.heapArray) - 1
		if (lastIndex % 2):
			index = int(lastIndex / 2)
		else:
			index = int(math.floor(lastIndex / 2) - 1)
		while index >= 0:
			self.heapify(index, len(self.heapArray))
			index -= 1

	def extract_max(self, size):
		toret = self.heapArray[0]
		self.heapArray[0] = self.heapArray.pop(size)
		self.heapify(0, size)
		return toret

	def __str__(self):
		return str(self.heapArray)


def heapSort(L):
	H = BinaryHeap(L)
	print(H)
	size = len(L) - 1
	while size:
		H.heapArray.insert(size, H.extract_max(size))
		size -= 1
	return H

def main():
	print(heapSort([7, 10, 20, 3, 4, 49, 50]))

if __name__ == '__main__':
	main()