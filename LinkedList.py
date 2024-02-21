# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 2/20/2024

"""
Description:
This module defines a LinkedList class with recursive implementations for add, remove, contains, insert, reverse, and to_plain_list methods. 
The LinkedList uses a private head node to manage its elements. Each Node in the list contains a data value and a reference to the next Node. 
The recursive methods provide a way to manipulate the list without iterative loops, adhering to a functional programming paradigm. 
The to_plain_list method returns a Python list representation of the LinkedList, preserving the order of elements.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def add(self, data, current=None):
        if current is None:
            current = self._head
        if self._head is None:
            self._head = Node(data)
        elif current.next is None:
            current.next = Node(data)
        else:
            self.add(data, current.next)

    def remove(self, data, current=None, prev=None):
        if current is None:
            current = self._head
        if self._head is not None:
            if current.data == data:
                if prev is not None:
                    prev.next = current.next
                else:
                    self._head = current.next
                return True
            elif current.next is None:
                return False
            return self.remove(data, current.next, current)
        return False

    def contains(self, data, current=None):
        if current is None:
            current = self._head
        if current is None:
            return False
        if current.data == data:
            return True
        return self.contains(data, current.next)

    def insert(self, index, data, current=None, count=0):
        if current is None:
            current = self._head
        if index == 0:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
            return
        if count == index - 1:
            temp = current.next
            current.next = Node(data)
            current.next.next = temp
            return
        if current.next is None:
            return
        self.insert(index, data, current.next, count + 1)

    def reverse(self, current=None, prev=None):
        if current is None:
            current = self._head
        if current.next is None:
            self._head = current
            current.next = prev
            return
        next_node = current.next
        current.next = prev
        self.reverse(next_node, current)

    def to_plain_list(self, current=None, result=None):
        if current is None:
            current = self._head
        if result is None:
            result = []
        if current is None:
            return result
        result.append(current.data)
        return self.to_plain_list(current.next, result)

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)