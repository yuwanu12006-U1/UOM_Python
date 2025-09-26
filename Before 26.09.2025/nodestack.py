# Node class represents one item in the list
class Node:
    def __init__(self, data):
        # store the given data
        self.data = data
        # next starts as nothing
        self.next = None

    def show(self):
        # print this node’s data
        print(self.data)


# Stack class uses linked Nodes to act like a stack (LIFO)
class Stack:
    def __init__(self):
        # head points to top node (none if empty)
        self.head = None
        # size counts how many nodes are stored
        self.size = 0
        # counter does the same as size here
        self.counter = 0

    def isEmpty(self):
        # return True if no items
        return self.counter == 0  # (P)

    def push(self, data):
        # make a new node for data
        node = Node(data)
        # we will have one more item now
        self.counter += 1

        # if stack was empty
        if self.isEmpty():
            # this new node is the head now
            self.head = node  # (Q)
        else:
            # link new node to old head
            node.next = self.head
            # update head to new node
            self.head = node  # (R)

        # track the added node
        self.size += 1

    def pop(self):
        # cannot remove from empty stack
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack")

        # take the top node
        node = self.head
        # head moves to next node
        self.head = self.head.next  # (S)
        # update counts down by one
        self.size -= 1
        self.counter -= 1
        # give back the popped node
        return node

    def getSize(self):
        # return number of items (size)
        return self.size

    def getCounter(self):
        # return number of items (counter)
        return self.counter
