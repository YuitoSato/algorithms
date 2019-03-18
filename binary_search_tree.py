class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def search(self, data):
        if data == self.data:
            return True
        elif data > self.data:
            return self.right.search(data)
        else:
            return self.left.search(data)

    def print(self):
        print(self.data)
        if self.left is not None:
            print(self.left.print())

        if self.right is not None:
            print(self.right.print())

n = Node(5)
n.insert(4)
n.insert(6)
n.insert(12)
n.insert(13)
n.insert(1)
n.insert(3)

print(n.print())
print(n.search(13))

