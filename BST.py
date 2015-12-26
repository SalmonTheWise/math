
class BSTNode:

    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def get_data(self):
        return self.data

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_right(self, new_right):
        self.right = new_right

    def set_prev(self, new_left):
        self.left = new_left



class BST:
    def __init__(self, data = None, t):
        self.root = data
        self.NodeType = NodeType
        self.psroot = self.NodeType(None, None)
        self.key = t

    def Add(self, elem):
        if self.root.get_data == None:
            self.root = BSTNode(elem)
        else:
            while True:
                curr = self.root
                if curr.get_data >= elem:
                    if curr.right != None:
                        curr = curr.right
                        continue
                    else:
                        curr.right = BSTNode(elem)
                        break
                else:
                    if curr.left != None:
                        curr = curr.left
                        continue
                    else:
                        curr.left = BSTNode(elem)
                        break

    def find(self, t):
        if self.root is None:
            return None
        else:
            return self.root.find(t)

    def Rebuild(self):
        self.root = self.psroot.left

    def Remove(self, t):
        node = self.find(t)
        deleted = self.root.Remove()
        self.Rebuild()
        return deleted

    def print(node):
        if node is None:
            print('node is none')
        else:
            print("node", node.key)
