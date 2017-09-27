class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insert(self,x,p):
        """Insert element x in the position after p"""
        temp = ListNode()
        temp.value = x
        temp.next = p.next
        p.next = temp

    def delete(self,p):
        """Delete the node following node p in the linked list."""
        if p.next != None:
        	p.next = p.next.next
        else:
        	print("No element after present after this node.")

    def print(self):
        """ Print all the elements of a list in a row."""
        temp = self.head.next
        toret = []
        while True:
        	toret.append(temp.value)
        	if temp.next == None:
        		break
        	temp = temp.next
        return toret

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp = self.head
        track = 0
        while True:
        	if track == i:
        		newTemp = ListNode()
        		newTemp.value = x
        		newTemp.next = temp.next
        		temp.next = newTemp
        		break
        	track = track + 1
        	if temp.next == None:
        		print("Not enough elements in the list.")
        		break
        	temp = temp.next

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head
        while True:
        	if temp.value == x:
        		return temp
        	if temp.next == None:
        		return None
        	temp = temp.next

    def isExisting(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head
        while True:
            if temp.value == x:
                return True
            if temp.next == None:
                return False
            temp = temp.next

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        temp = self.head
        track = 0
        while temp.next != None:
        	track = track + 1
        	temp = temp.next
        return track

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next == None:
        	return True
        return False

    def reverse(self):
    	current = self.head.next
    	prev = None
    	while current != None:
    		next_one = current.next
    		current.next = prev
    		prev = current
    		current = next_one
    	self.head.next = prev

class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,k="",val=None,nxt=None):
        self.key=k
        self.value=val
        self.next=nxt

class HashTable:
    def __init__(self, leng=30):
        self.length = leng
        self.T = [None for i in range(self.length)]

    def insert(self, strr):
        insertKey = hashFunc(strr, self.length)
        if self.T[insertKey] == None:
            self.T[insertKey] = LinkedList()
        index = self.T[insertKey].len()
        self.T[insertKey].insertAtIndex(strr, index)

    def keys(self):
        positions = []
        for i in range(len(self.T)):
            if self.T[i] != None:
                positions.append(i)
        return positions

    def search(self, strr):
        searchKey = hashFunc(strr, self.length)
        if self.T[searchKey] != None:
            return self.T[searchKey].isExisting(strr)
        return False

def hashFunc(string, leng):
    summ = 0
    for i in string:
        summ += ord(i)
    return (summ % leng)

def main():
    table = HashTable()
    table.insert("hello")
    table.insert("gibberish")
    table.insert("hola")
    #print(table.T[table.keys()[1]].print())
    print(table.search("gibberish"))
    print(table.keys())

if __name__ == '__main__':
    main()