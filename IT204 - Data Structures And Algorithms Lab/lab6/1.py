class AVLSearchTree:
    def __init__(self, r=None):
        self.root = TreeNode(k=r)
        self.root.height = 1
        self.preorder = []
        self.inorder = []
        self.postorder = []
    
    def insert(self, k, x):
        if k < x.key:
            if x.left_child:
                self.insert(k, x.left_child)
            else:
                x.left_child = TreeNode(k=k, p=x)
                self.bottomUpUpdateHeights(x.parent)
        else:
            if x.right_child:
                self.insert(k, x.right_child)
            else:
                x.right_child = TreeNode(k=k, p=x)
                self.bottomUpUpdateHeights(x.parent)

    def bottomUpUpdateHeights(self, x):
        if not x:
            return
        leftHeight = self.getHeight(x.left_child)
        rightHeight = self.getHeight(x.right_child)
        if (leftHeight - rightHeight) not in range(-1,2):
            self.rebalance(x)
        else:
            newHeight = max(leftHeight, rightHeight) + 1
        if x.parent:
            self.bottomUpUpdateHeights(x.parent)

    def delete(self, k):
        node = self.search(k, self.root)
        if not node:
            return
        if node.isLeaf() or node.hasOneChild():
            self.deleteNode(node)
            self.bottomUpUpdateHeights(node.parent)
        else:
            successorNode = self.successor(node)
            node.key = successorNode.key
            self.deleteNode(successorNode)
            self.bottomUpUpdateHeights(successorNode)

    def deleteNode(self, x):
        if x.isLeftChild():
            if x.left_child:
                x.parent.left_child = x.left_child
            else:
                x.parent.left_child = x.right_child
        else:
            if x.left_child:
                x.parent.right_child = x.left_child
            else:
                x.parent.right_child = x.right_child

    def rebalance(self, x):
        if (self.getHeight(x.left_child) > self.getHeight(x.right_child)) and (self.getHeight(x.left_child.left_child) > self.getHeight(x.left_child.right_child)):
            self.rightRotate(x)
        elif (self.getHeight(x.left_child) > self.getHeight(x.right_child)) and (self.getHeight(x.left_child.right_child) > self.getHeight(x.left_child.left_child)):
            self.leftRotate(x.left_child)
            self.rightRotate(x)
        elif (self.getHeight(x.right_child) > self.getHeight(x.left_child)) and (self.getHeight(x.right_child.left_child) > self.getHeight(x.right_child.right_child)):
            self.rightRotate(x.right_child)
            self.leftRotate(x)
        elif (self.getHeight(x.right_child) > self.getHeight(x.left_child)) and (self.getHeight(x.right_child.right_child) > self.getHeight(x.right_child.left_child)):
            self.leftRotate(x)

    def rightRotate(self, x):
        if x.isLeftChild():
            x.parent.left_child = x.left_child
        else:
            x.parent.right_child = x.left_child
        x.left_child.parent = x.parent
        x.parent = x.left_child
        x.left_child = x.left_child.right_child
        x.parent.right_child = x

    def getHeight(self, x):
        if x:
            return x.height
        else:
            return 0

    def leftRotate(self, x):
        if x.isLeftChild():
            x.parent.left_child = x.right_child
        else:
            x.parent.right_child = x.right_child
        x.right_child.parent = x.parent
        x.parent = x.right_child
        x.right_child = x.right_child.left_child
        x.parent.left_child = x

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
                return x

    def maximum(self, x):
        if (x == None):
            return None
        else:
            if x.right_child:
                return self.maximum(x.right_child)
            else:
                return x

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
        self.postorder = []
        self.postorder_traversal(self.root)
        print(self.postorder)

    def printPrefix(self):
        self.preorder = []
        self.preorder_traversal(self.root)
        print(self.preorder)


class TreeNode:
    def __init__(self, k=None, p=None):
        self.parent = p
        self.left_child = None
        self.right_child = None
        self.key = k
        self.height = 1

    def isLeftChild(self):
        return self.parent.left_child == self

    def isRightChild(self):
        return self.parent.right_child == self

    def isChild(self, x):
        return (x.right_child == self) or (x.left_child == self)

    def isLeaf(self):
        if (not self.right_child) and (not self.left_child):
            return True
        return False

    def hasOneChild(self):
        if (not self.right_child and self.left_child) and (self.right_child and not self.left_child):
            return True
        return False

def main():
    B = AVLSearchTree(13)
    B.printPrefix()
    B.insert(10, B.root)
    B.printPrefix()
    B.insert(15, B.root)
    B.printPrefix()
    B.insert(5, B.root)
    B.printPrefix()
    B.insert(11, B.root)
    B.printPrefix()
    B.insert(16, B.root)
    B.printPrefix()
    B.insert(4, B.root)
    B.printPrefix()
    B.insert(6, B.root)
    B.printPrefix()
    B.insert(7, B.root)
    B.printPrefix()
    print()
    B.printPostfix()
    print(B.maximum(B.root).key)
    print(B.minimum(B.root).key)
    print(B.successor(B.root).key)
    print(B.predecessor(B.root).key)
    print(B.search(6, B.root).key == 6)
    print()
    B.printPrefix()
    B.delete(16)
    B.printPrefix()
    B.delete(7)
    B.printPrefix()

if __name__ == '__main__':
    main()