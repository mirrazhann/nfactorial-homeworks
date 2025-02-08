from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """

        if 0 <= index <= self.capacity - 1:
            self.array[index] = value
        else:
             raise ValueError(f"{index} is not in array`s diapazone")
 
    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        return self.array[index]

class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self.array = []

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
        else:
            raise ValueError (f"{index} is not in array`s diapazone")

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """
        if 0 <= index <= len(self.array):
            del self.array[index]
        else:
            raise ValueError (f"{index} in not in array`s diapazone")

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        return self.array[index]

class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        if position < 0:
            raise ValueError ("Error! Invalid position")

        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        while current and count < position-1:
            current = current.next
            count += 1

        if current == None:
            raise ValueError ("Error! Invalid position")
        else:
            new_node.next = current.next
            current.next = new_node
            


    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        if not self.head:
            raise ValueError ("Error! empty list")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current:
            if current.value == value:
                current = current.next
                return
        

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        if not self.head:
            raise ValueError ("Error! Empty list")
        else:
            current = self.head
            while current:
                if current.value == value:
                    return current
                else:
                    current = current.next
            return None


    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        if not self.head:
            return 0
        else:
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            return count


    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        if not self.head:
            return True
        return False

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        if not self.head:
            raise ValueError (f"The list has not nodes")

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        

    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  
            current.next = prev  
            prev = current  
            current = next_node  
        
        self.head = prev
    
    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        if not self.head:
            raise ValueError (f"The list has not nodes")
        else:
            return self.head
    
    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        if not self.head:
            raise ValueError (f"The list has not nodes")
        else:
            current = self.head
            while current.next:
                current = current.next
            return current

class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = self.tail = new_node
            print(self.head.value)
            print(self.tail.value)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1



    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        new_node = DoubleNode(value)
        if position < 0 or position > self._size:
            raise ValueError ("Error! Invalid position")

        if position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self._size += 1
                return
            else:
                self.append(value)
                self._size += 1
                return
        else:
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
            if new_node.next is None:
                self.tail = new_node
            self._size += 1
            return

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        if not self.head:
            raise ValueError ("Error! empty list")

        current = self.head
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                    else:
                        self.head = None 
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                self._size -=1
                return
            current = current.next

        


    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        if not self.head:
            raise ValueError ("Error! Empty list")
        else:
            current = self.head
            while current:
                if current.value == value:
                    return current
                else:
                    current = current.next
            return None


    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        if self._size == 0:
            return True
        return False

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        temp = None
        current = self.head
        self.tail = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev
    
    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
        if not self.head:
            raise ValueError (f"The list has not head")
        else:
            return self.head
    
    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """
        if not self.head:
            raise ValueError (f"The list has not tail")
        else:
            return self.tail

class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.queue.append(value)

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.is_empty():
            raise IndexError ("Error! Empty queue")
        else:
            return self.queue.pop(0)

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError ("Error! Empty queue")
        else:
            return self.queue[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """
        self.value = value
        self.right = None
        self.left = None
        

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """
        def _insert(node, value):
            if node is None:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        
        self.root = _insert(self.root, value)

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """
        def _delete(node, value):
            if node is None:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.minimum(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            return node
        
        self.root = _delete(self.root, value)

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """
        if self.is_empty() == True:
            return "Empty Binary Tree"

        current = self.root
        while current:
            if current.value == value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return "No result"

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result
    
    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        
        return _size(self.root)

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """
        if self.root == None:
            return True
        else:
            return False

    def height(self) -> int:
        """
        Returns the height of the tree.
        """
        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        
        return _height(self.root)


    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """
        result = []
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
        _postorder(self.root)
        return result

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """
        current = self.root
        while current and current.left:
            current = current.left
        return current


    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
        current = self.root
        while current and current.right:
            current = current.right
        return current
    
    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """
        def _is_valid(node, low, high):
            if node is None:
                return True
            if node.value <= low or node.value >= high:
                return False
            return _is_valid(node.left, low, node.value) and _is_valid(node.right, node.value, high)
        
        return _is_valid(self.root, float('-inf'), float('inf'))

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        current = lst[i]
        j = i-1
        while j >= 0 and lst[j] > current:
            lst[j+1] = lst[j]
            j -= 1
        lst[j + 1] = current
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        temp_i = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[temp_i]:
                temp_i = j
        lst[i], lst[temp_i] = lst[temp_i], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    check = True
    while check:
        check = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                check = True
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    step = len(lst)//2
    while step > 0:
        for i in range(step, len(lst)):
            temp = lst[i]
            j = i
            while j >= step and lst[j - step] > temp:
                lst[j] = lst[j - step]
                j -= step
            lst[j] = temp
        step = step//2
    return lst


def merge_sort(lst: List[int]) -> List[int]:
    pass

def quick_sort(lst: List[int]) -> List[int]:
    pass
