class Link:
    # the link object has two attribute key for storing the data and next to link to the next node in the list
    def __init__(self, key=None):
        self.key = key
        self.next = None


class LinkedList:
    # init the head of the list to be none
    # take O(1) time
    def __init__(self):
        self.head = None

    # return ture if the list is empty
    # take O(1) time
    def empty(self):
        return self.head is None

    # insert a new node with the value key at the begging of the list
    # take O(1)
    def insert(self, key):
        # if the list is empty set head to be the node with the value key
        if self.empty():
            self.head = Link(key)
        else:
            newLink = Link(key)
            newLink.next = self.head
            self.head = newLink

    # delete the element with the value key and return the node
    # take O(n) time
    def delete(self, key):
        ptr = self.head
        while ptr.next.key != key or ptr.next:
            ptr = ptr.next
        ptr.next = ptr.next.next
        return ptr

    # delete the first element of the list and return the node
    # take O(1) time
    def pop(self):
        if not self.empty():
            ptr = self.head
            self.head = self.head.next
            return ptr
        return None

    # return the node with the value key in the list, or None if the node doesn't exist
    # take O(n) time
    def find(self, key):
        ptr = self.head
        while ptr and ptr.key != key:
            ptr = ptr.next
        return ptr

    # return the len of the list
    # take O(n) time
    def __len__(self):
        size = 0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            size += 1
        return size

    # return the size of the list
    # take O(n) time
    def size(self):
        return len(self)

    # return true is the list is an ordered list
    # take O(n) time
    def is_sorted(self):
        ptr = self.head
        if self.empty():
            return True
        num1 = self.head.key
        while ptr:
            num2 = ptr.key
            if num1 > num2:
                return False
            ptr = ptr.next
            num1 = num2
        return True

    # insert a new element after link
    # take O(n) time
    @staticmethod
    def insert_after(link: Link, key):
        newLink = Link(key)
        newLink.next = link
        link.next = newLink
