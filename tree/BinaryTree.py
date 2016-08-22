class BinaryTree(object):
    def __init__(self, newobject):
        self.root = newobject
        self.left = None
        self.right = None

    def insertleft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertright(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp

    def getrightnode(self):
        return self.right

    def getleftnode(self):
        return self.left

    def getrootvalue(self):
        return self.root

    def setrootvalue(self, val):
        self.root = val


the_tree = BinaryTree(1)
the_tree.insertleft(3)
the_tree.insertleft(5)
the_tree.insertright(13)
the_tree.insertright(15)
print the_tree.getrightnode().getrightnode().getrootvalue()