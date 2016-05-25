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
        # Initialize the node attributes
        self.elem = elem
        self.next = next
    
    def __str__(self):
        # Return the string representation of the node 
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


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """
    
    def __init__(self, elements=None):
        # Initialize values for start & end, and link the elements together
        self.start = None
        self.end = None
        
        # If there are any elements, convert each one to a node and link them
        #  together in sequence
        if elements:
            for elem in elements:
                this = Node(elem)
                
                # Initialize the start node if it has not already been done
                if not self.start:
                    self.start = this
                
                # If there are already any nodes, link the current one to the
                #  last one in the list
                if self.end:
                    self.end.next = this
                
                # Make this node the last one
                self.end = this
    
    def __str__(self):
        # Make a list of the string representations of the nodes
        node_strings = [str(node) for node in self]
        
        # Return list of elements separated by commas in a set of brackets
        return '[' + ', '.join(node_strings) + ']'
    
    def __repr__(self):
        return 'LinkedList({})'.format(str(self))
    
    def __len__(self):
        elem_count = 0
        for _ in self:
            elem_count += 1
        
        return elem_count
    
    def __iter__(self):
        return iter(_get_node_from_list(self.start))
        # Implemented in Python 3:
        # yield from _get_node_from_list(self.start)
    
    def __getitem__(self, index):
        # Raise a TypeError if the index is not an integer
        if not isinstance(index, int):
            err_msg = '"index" must be an integer ({} given)'
            raise TypeError(err_msg.format(type(index)))
        
        # Iterate through the items and return the one with the right index
        node_index = 0
        for node in self:
            if index == node_index:
                return node
            node_index += 1
        
        # Raise an IndexError if no item matches the index supplied
        err_msg = 'LinkedList index out of range'
        raise IndexError(err_msg)
    
    def __add__(self, other):
        # Raise a TypeError if anything other than a LinkedList is added
        if not isinstance(other, LinkedList):
            err_msg = 'Only another LinkedList object may be added \
                to a LinkedList'
            raise TypeError(err_msg)
        
        # Build a new list from scratch
        new_list = []
        for node in self:
            new_list.append(node.elem)
        for node in other:
            new_list.append(node.elem)
        
        # Return the LinkedList version of it
        return LinkedList(new_list)
    
    def __iadd__(self, other):
        # Raise a TypeError if anything other than a LinkedList is added
        if not isinstance(other, LinkedList):
            err_msg = 'Only another LinkedList object may be added \
                to a LinkedList'
            raise TypeError(err_msg)
        
        # The nodes list prevents the LinkedList from growing infinitely large 
        #  if it is added to itself
        nodes = [node for node in other]
        for node in nodes:
            self.append(node.elem)
        
        return self
    
    def __eq__(self, other):
        # If other is not a LinkedList, they are not equal
        if not isinstance(other, LinkedList):
            return False
        
        # If the lists have unequal length, they are not equal
        if len(self) != len(other):
            return False
        
        # If there are any nodes in the list whose elements are different,
        #  they are not equal
        for self_node, other_node in zip(self, other):
            if self_node.elem != other_node.elem:
                return False
        
        # If the lists have equal length, and every node is the same, they are
        #  equal
        return True
    
    def append(self, elem):
        # Make a node of the element to be appended
        this = Node(elem)
        
        # Make this node "next" for the previously last node
        if self.end:
            self.end.next = this
        else:
            self.start = this
        
        # Make this the end element
        self.end = this
    
    def count(self):
        return len(self)
    
    def pop(self, index=None):
        # Set the index to the last element, if no index is passed
        if index is None:
            index = len(self) - 1
        
        # Get the node that matches the index
        node = self[index]
        
        # If popping the first node, make the next node the start
        if node is self.start:
            self.start = node.next
        
        # If not popping the first node, point the previous node to the
        #  following one
        else:
            self[index - 1].next = node.next
        
        # If the end was popped off and there are more nodes, reset the end
        if node is self.end and self:
            self.end = self[len(self) - 1]
        
        return node.elem


# Generator for nodes in a linked list
def _get_node_from_list(start_node):
    node = start_node
    while node:
        this, node = node, node.next
        yield this
