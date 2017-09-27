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
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ',L.print())
    L.insert(12,L.head.next)
    print('List is: ',L.print())
    L.insert(2,L.head)
    print('List is: ',L.print())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',L.print())
    L.delete(L.head.next)
    print('List is: ',L.print())
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ',L.print())
    L.reverse()
    print('List is: ',L.print())

if __name__ == '__main__':
    main()