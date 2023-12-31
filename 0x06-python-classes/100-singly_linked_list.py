#!/usr/bin/python3

"""Defines nodes for a singly linked list"""


class Node:
    """Defines a node of a singly linked list

    Attributes:
        data (int): data in node
        next_node (Node): next node in singly linked list

    """

    def __init__(self, data, next_node=None):
        """Initializes the node

        Args:
            data (int): data in node
            next_node (Node): next node in singly linked list
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: gets the data of the current node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: gets the next node in the singly linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines the list

    Attributes:
        head (Node): first node in list

    """

    def __init__(self):
        """Initializes the list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node in the corrext sorted position in the list

        Args:
            value (Node): new node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of a singly linked list"""
        dataset = []
        tmp = self.__head
        while tmp is not None:
            dataset.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(dataset))
