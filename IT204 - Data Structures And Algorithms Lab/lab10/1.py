class GraphNode:
	def __init__(self, k):
		self.key = k
		self.color = 'WHITE'
		self.pred = None
		self.start = None
		self.end = None

	def __str__(self):
		return str([self.key, self.color, self.start, self.end])

class Graph:
	def __init__(self, v):
		self.vNodes = [GraphNode(i) for i in range(v)]
		self.vertices = v
		self.adjMat = [[0 for a in range(self.vertices)] for b in range(self.vertices)]
		self.adjList = [[] for i in range(self.vertices)]

	def add(self, first, second):
		self.adjMat[first][second] = self.adjMat[second][first] = 1
		self.adjList[first].append(second)
		self.adjList[second].append(first)

	def printMat(self):
		for i in range(self.vertices):
			for j in range(self.vertices):
				print(str(self.adjMat[i][j]) + " ", end='')
			print()

	def printList(self):
		for i in range(self.vertices):
			print("Vertex " + str(i + 1) + ": ", end='')
			for j in self.adjList[i]:
				print(str(j) + ", ", end='')
			print(str(None))

def DFS(G, u):
	global timestamp
	G.vNodes[u].start = timestamp
	timestamp += 1
	G.vNodes[u].color = 'GREY'
	for v in G.adjList[G.vNodes[u].key]:
		if G.vNodes[v].color == 'WHITE':
			print(G.vNodes[v])
			DFS(G, v)
			G.vNodes[v].pred = G.vNodes[u]
			print(G.vNodes[v])
	G.vNodes[u].color = 'BLACK'
	G.vNodes[u].end = timestamp
	timestamp += 1

def main():
	global timestamp
	n = int(input("Enter the number of vertices: "))
	G = Graph(n)
	while True:
		option = int(input("Enter 1 to enter an edge and 2 to stop input: "))
		if option == 1:
			v1 = int(input("Enter vertex 1: "))
			v2 = int(input("Enter vertex 2: "))
			G.add(v1, v2)
		elif option == 2:
			break
		else:
			print("Wrong input!")
	G.printMat()
	print()
	G.printList()
	source = int(input("Enter the source vertex: "))
	print(G.vNodes[source])
	G.vNodes[source].color = 'BLACK'
	DFS(G, source)
	G.vNodes[source].end = timestamp
	print(G.vNodes[source])

if __name__ == '__main__':
	global timestamp
	timestamp = 1
	main()