class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.length()

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value, self.root)
        self.size += 1

    def _put(self, key, value, currentnode):
        if key < currentnode.key:
            if currentnode.hasleft():
                self._put(key, value, currentnode.left)
            else:
                currentnode.left = TreeNode(key, value, parent=currentnode)
        else:
            if currentnode.hasright():
                self._put(key, value, currentnode.right)
            else:
                currentnode.right = TreeNode(key, value, parent=currentnode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, currentnode):
        if currentnode.key == key:
            return currentnode
        elif currentnode.key > key:
            if currentnode.hasleft:
                return self._get(key, currentnode.left)
        else:
            if currentnode.hasright:
                return self._get(key, currentnode.right)
        return None

    def __getitem__(self, key):
        self.get(key)

    def __contains__(self, key):
        if self.__getitem__(key):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            currentnode = self.get(key)
            if currentnode:
                self._delete(currentnode)
                print key + " is deleted"
            else:
                raise "no such node : " + key
            self.size -= 1
        elif self.size == 1 and self.get(key) == self.root:
            self.root = None
            self.size -= 1
        else:
            raise "No Node error"

    def _delete(self, node):
        if node.hasbothchild():
            tmp = node
            node = node.left
            while node.hasright:
                node = node.right
            if node.hasright:
                node.parent.right = node.right
            if node.hasleft:
                node.parent.right.left = node.left
            node.parent = tmp.parent
            node.left = tmp.left
            node.right = tmp.right
        if node.hasleft():
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        if node.hasright():
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        if node.isleaf():
            node.parent = None

class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def hasleft(self):
        return self.left

    def hasright(self):
        return self.right

    def isleft(self):
        return self.parent.left

    def isright(self):
        return self.parent.right

    def isleaf(self):
        return not (self.left or self.right)

    def isroot(self):
        return self.parent is None

    def hasanychild(self):
        return self.left or self.right

    def hasbothchild(self):
        return self.left and self.right

    def replacenode(self, k, v, lc, rc):
        self.key = k
        self.value = v
        self.left = lc
        self.right = rc
        if self.hasleft():
            self.left.parent = self
        if self.hasright():
            self.right.parent = self
