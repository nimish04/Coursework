class Node:
	def __init__(self, k=None):
		self.key = k
		self.children = {}
		self.isWord = False
		self.parent = None

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		currentNode = self.root
		for letter in word:
			newKey = ord(letter) - ord('a')
			if newKey not in currentNode.children.keys():
				currentNode.children[newKey] = Node(letter)
			currentNode.children[newKey].parent = currentNode
			currentNode = currentNode.children[newKey]
		currentNode.isWord = True

	def search(self, word):
		currentNode = self.root
		for letter in word:
			newKey = ord(letter) - ord('a')
			if newKey not in currentNode.children.keys():
				return False
			currentNode = currentNode.children[newKey]
		return currentNode.isWord

def main():
	T = Trie()
	T.insert("hey")
	T.insert("hello")
	print(T.search("hey"))
	print(T.search("he"))
	T.insert("he")
	print(T.search("he"))
	print(T.search("hello"))

if __name__ == '__main__':
	main()