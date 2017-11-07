import math

class GraphNode:
	def __init__(self, k):
		self.key = k
		self.dist = math.inf

	def __str__(self):
		return str([self.key, self.dist])

class Graph:
	def __init__(self, v):
		self.vNodes = [GraphNode(i) for i in range(v)]
		self.vertices = v
		self.adjMat = [[(0, None) for a in range(self.vertices)] for b in range(self.vertices)]
		self.adjList = [[] for i in range(self.vertices)]

	def add(self, first, second, cost):
		self.adjMat[first][second] = self.adjMat[second][first] = (1, cost)
		self.adjList[first].append((second, cost))
		self.adjList[second].append((first, cost))

	def printMat(self):
		for i in range(self.vertices):
			for j in range(self.vertices):
				print(str(self.adjMat[i][j][0]) + " ", end='')
			print()

	def printList(self):
		for i in range(self.vertices):
			print("Vertex " + str(i) + ": ", end='')
			for j in self.adjList[i]:
				print(str(j) + ", ", end='')
			print(str(None))

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
			if (parent >= 0) and (self.heapArray[index].dist < self.heapArray[parent].dist):
				self.heapArray[index], self.heapArray[parent] = self.heapArray[parent], self.heapArray[index]
			else:
				break
			index = parent
			if (index % 2):
				parent = int(index / 2)
			else:
				parent = int(math.floor(index / 2) - 1)

	def minimum(self):
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
			if leftChildExists and rightChildExists and (self.heapArray[index].dist > self.heapArray[leftChild].dist) and (self.heapArray[index].dist > self.heapArray[rightChild].dist):
				if self.heapArray[leftChild].dist < self.heapArray[rightChild].dist:
					child = leftChild
				else:
					child = rightChild
			elif leftChildExists and (self.heapArray[index].dist > self.heapArray[leftChild].dist):
				child = leftChild
			elif rightChildExists and (self.heapArray[index].dist > self.heapArray[rightChild].dist):
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
		index = len(self.heapArray) - 1
		while index >= 0:
			if 2 * index < len(self.heapArray):
				self.heapify(index)
			index -= 1

	def extract_min(self):
		toret = self.heapArray[0]
		self.heapArray[0] = self.heapArray.pop(-1)
		self.heapify(0)
		return toret

	def updatePriority(self, G):
		for n in range(len(self.heapArray)):
			self.heapArray[n] = G.vNodes[self.heapArray[n].key]
		self.build_heap()

	def __str__(self):
		return str(self.heapArray)

def main():
	# Graph initialize

	n = int(input("Enter the number of vertices: "))
	G = Graph(n)
	while True:
		option = int(input("Enter 1 to enter an edge and 2 to stop input: "))
		if option == 1:
			v1 = int(input("Enter vertex 1: "))
			v2 = int(input("Enter vertex 2: "))
			cost = int(input("Enter the cost of this edge: "))
			G.add(v1, v2, cost)
		elif option == 2:
			break
		else:
			print("Wrong input!")

	# End graph initialize
	
	G.printMat()
	print()
	G.printList()
	source = int(input("Enter the source vertex: "))
	sink = int(input("Enter the destination vertex: "))
	G.vNodes[source].dist = 0
	H = BinaryHeap()	
	for node in G.vNodes:
		H.insert(node)
	while len(H.heapArray) > 1:
		w = H.extract_min()
		for v in G.adjList[w.key]:
			if w.dist + v[1] < G.vNodes[v[0]].dist:
				G.vNodes[v[0]].dist = w.dist + v[1]
				H.updatePriority(G)
	print("Shortest path from vertex " + str(source) + " to vertex " + str(sink) + " : " + str(G.vNodes[sink].dist))

"""
	To test run the algorithm, use the code below in the 'Graph initialize' block

	# listt = [[0,1,7], [0,2,9], [0,5,14], [1,2,10], [2,5,2], [1,3,15], [2,3,11], [3,4,6], [5,4,9]]
	# listt = [[0,1,4],[0,7,8],[1,7,11],[7,6,1],[7,8,7],[1,2,8],[2,8,2],[8,6,6],[6,5,2],[2,5,4],[2,3,7],[3,5,14],[3,4,9],[5,4,10]]
	G = Graph(len(listt))
	for a in listt:
		G.add(a[0],a[1],a[2])
"""

if __name__ == '__main__':
	main()
