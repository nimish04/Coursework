class Node:
	def __init__(self, k=None, occurences=[]):
		self.key = k
		self.children = {}
		self.isWord = False
		self.parent = None
		self.indices = occurences

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word, ind):
		currentNode = self.root
		for letter in word:
			newKey = ord(letter) - ord('a')
			if newKey not in currentNode.children.keys():
				currentNode.children[newKey] = Node(letter,[])
			currentNode.children[newKey].parent = currentNode
			currentNode = currentNode.children[newKey]
		currentNode.isWord = True
		currentNode.indices.append(ind)

	def search(self, word):
		currentNode = self.root
		for letter in word:
			newKey = ord(letter) - ord('a')
			if newKey not in currentNode.children.keys():
				return False
			currentNode = currentNode.children[newKey]
		return currentNode.isWord

	def getOccurences(self, word):
		currentNode = self.root
		for letter in word:
			newKey = ord(letter) - ord('a')
			if newKey not in currentNode.children.keys():
				return False
			currentNode = currentNode.children[newKey]
		return currentNode.indices

def main():
	T = Trie()
	sentence = "bring back bring back bring back the champions to me to me"
	tracker = 0
	for i in sentence.split(" "):
		T.insert(i, tracker)
		tracker += len(i) + 1
	print(T.getOccurences("back"))

if __name__ == '__main__':
	main()