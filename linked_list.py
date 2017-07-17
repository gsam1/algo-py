class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def __repr__(self):
        '''
        More of a string reprisentation than accessable list
        '''
        curr = self.head
        printable = ''
        while curr is not None:
            printable += str(curr.data)
            printable += '->'
            curr = curr.next

        printable += 'None'
        return printable

    def add(self, item):
        '''
        Takes one item and adds it to the linked list
        '''
        curr = Node(item)
        curr.next = self.head
        self.head = curr

    def remove(self, item):
        '''
        Removes a singular item from the linked list.
        If there are duplicates it removes the first one.
        '''
        curr = self.head
        prev = None
        found = False
        while not Found:
            if curr.data == item:
                found = True
            else:
                prev = curr
                curr = curr.next

        if prev == None:
            self.head = curr.next
        else:
            prev.next = curr.next

    def size(self):
        '''
        Method for getting the size of the linked list.
        '''
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        return count
