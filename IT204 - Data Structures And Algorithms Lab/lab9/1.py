class Graph:
    def __init__(self, v):
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

def main():
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
    G.printList()

if __name__ == '__main__':
    main()
