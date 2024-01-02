class Node:
    def __init__(self, v=None, p=None):
        self.keys = [v]
        self.parent = p
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def isleaf(self, cur_node):
        if len(cur_node.children) == 0:
            return True
        else:
            return False

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node, value):
        if cur_node is not None:
            if len(cur_node.keys) < 3:
                if len(cur_node.keys) == 1:
                    check = self.isleaf(cur_node)
                    if check:
                        cur_node.keys.append(value)
                        cur_node.keys.sort()
                    else:
                        if value > cur_node.keys[0]:
                            self._insert(cur_node.children[-1], value)
                        elif value < cur_node.keys[0]:
                            self._insert(cur_node.children[0], value)
                elif len(cur_node.keys) == 2:
                    check = self.isleaf(cur_node)
                    if check:
                        cur_node.keys.append(value)
                        cur_node.keys.sort()
                    else:
                        if value > cur_node.keys[1]:
                            self._insert(cur_node.children[-1], value)
                        elif value < cur_node.keys[0]:
                            self._insert(cur_node.children[0], value)
                        elif cur_node.keys[0] < value and value < cur_node.keys[1]:
                            self._insert(cur_node.children[1], value)
            if len(cur_node.keys) == 3:
                self.split(cur_node)

    def split(self, cur_node):
        self.root.keys.sort()
        if cur_node.parent == None:
            lefttmp = Node(cur_node.keys.pop(0))
            righttmp = Node(cur_node.keys.pop(-1))
            newroot = Node(cur_node.keys.pop(0))
            if len(cur_node.children) > 0:
                if len(cur_node.children) == 2:
                    lefttmp.children.append(cur_node.children[0])
                    righttmp.children.append(cur_node.children[1])
                    lefttmp.children[0].parent = lefttmp
                    righttmp.children[0].parent = righttmp
                elif len(cur_node.children) == 4:

                    lefttmp.children.append(cur_node.children[0])
                    lefttmp.children.append(cur_node.children[1])
                    righttmp.children.append(cur_node.children[2])
                    righttmp.children.append(cur_node.children[3])

                    lefttmp.children[0].parent = lefttmp
                    lefttmp.children[1].parent = lefttmp
                    righttmp.children[0].parent = righttmp
                    righttmp.children[1].parent = righttmp

            lefttmp.parent = newroot
            righttmp.parent = newroot
            newroot.children.append(lefttmp)
            newroot.children.append(righttmp)
            self.root = newroot
        else:
            cur_node.parent.keys.append(cur_node.keys.pop(1))
            cur_node.parent.keys.sort()
            tmp = Node(cur_node.keys.pop(0))
            tmp2 = Node(cur_node.keys.pop(0))
            tmp.parent = cur_node.parent
            tmp2.parent = cur_node.parent
            cur_node.parent.children.append(tmp)
            cur_node.parent.children.append(tmp2)
            cur_node.parent.children.remove(cur_node)
            sorted_nodes = sorted(cur_node.parent.children, key=lambda x: x.keys)
            cur_node.parent.children = sorted_nodes
            if len(cur_node.parent.keys) == 3:
                self.split(cur_node.parent)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, cur_node):
        if cur_node is not None:
            if len(cur_node.children) == 3:
                self._printTree(cur_node.children[0])
                self._printTree(cur_node.children[1])
                self._printTree(cur_node.children[2])
                print('Node:', cur_node.keys)
                for node in cur_node.children:
                    print('   children:', node.keys)
            elif len(cur_node.children) == 2:
                self._printTree(cur_node.children[0])
                self._printTree(cur_node.children[1])
                print('Node:', cur_node.keys)
                for node in cur_node.children:
                    print('   children:', node.keys)
            elif len(cur_node.children) == 1:
                self._printTree(cur_node.children[0])
                print('Node:', cur_node.keys)
                for node in cur_node.children:
                    print('   children:', node.keys)
            elif len(cur_node.children) == 0:
                print('Node:', cur_node.keys)
                for node in cur_node.children:
                    print('   children:', node.keys)


tree = Tree()
lst = [13, 7, 24, 15, 4, 29, 20, 16, 19, 1, 5, 22, 17]
for item in lst:
    tree.insert(item)
tree.printTree()
