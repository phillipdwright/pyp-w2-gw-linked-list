class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """
    
    def __init__(self, elem, next=None):
        # Initialize Node attributes
        self.elem = elem
        self.next = next
    
    def __str__(self):
        # Return the string representation of Node 
        return str(self.elem)
    
    def __eq__(self, other):
        # Return a truth value for "self == other"
        # Not sure if we need the "if" statements.
        if self.next is None and other.next is not None:
            return False
        if self.next is not None and other.next is None:
            return False
        return (self.elem == other.elem)
    
    def __repr__(self):
        return "Node({}, {})".format(self.elem, self.next)

# n = Node([])
# repr(n) # will return the value returned in __repr__(n)
# eval(repr(n)) == n

# n = Node(1)
# p = Node(1)

# n == p
# # n is self, p is other
# # __eq__(n, p):
#   n.elem == p.elem ??

# l = LinkedList([1, 5, 10])

# l.start = None
# l.end = None
# this = Node(1)
# self.start = this # Node(1)
# self.end = this # Node(1)
# this = Node(5)
# self.end.next = this # Node(1).next = Node(5)
# self.end = this # Node(5)
# this = Node(10)
# self.end.next = this # Node(5).next = Node(10)
# self.end = this # Node(10)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        # Initialize values for start, end, & created Nodes
        self.start = None
        self.end = None
        self.elements = elements # Just needed for __iter__()
        for elem in elements:
            this = Node(elem)
            if not self.start:
                self.start = this
            if self.end:
                self.end.next = this
            self.end = this
        # Initialize the value to be tracked by the iterator
        self.current = self.start
            

    def __str__(self):
        #node_strings = [str(node) for node in self.nodes]
        #return "[" + ", ".join(node_strings) + "]"
        pass

    def __len__(self):
        pass
        #return len(self.nodes)

    def __iter__(self):
        # behavior for restarting iteration at the beginning
        return LinkedList(self.elements)
    
    def __next__(self):
        # if self.current is None:
        #     raise StopIteration()
        # this, self.current = self.current, self.current.next
        # return this
        
        # Implemented in Python 3:
        # yield from get_elem_from_node(self.start)
        for elem in get_elem_from_node(self.start):
            return elem

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for self_node, other_node in zip(self.nodes, other.nodes):
            if self_node.elem != other_node.elem:
                return False
                
    next = __next__

    def append(self, elem):
        this = Node(elem)
        if self.end:
            self.end.next = this
        self.end = this
        self.nodes.append(this)
        # Set "next" for the previous element

    def count(self):
        return len(self)
        

    def pop(self, index=None):
        pass

# Generator
def get_elem_from_node(start_node):
    node = start_node
    while node:
        elem, node = node.elem, node.next
        yield elem