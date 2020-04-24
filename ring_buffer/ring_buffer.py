from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check if the ring buffer is at capacity, if not, we want to add the item to the tail
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            # Assign the head of the list to the current value
            self.current = self.storage.head
        # Also need to have a check to determine if ring buffer is at capacity, if so, we need to drop the oldest item off the end before inserting the new item.
        elif len(self.storage) == self.capacity:
            # Assign current head of list to oldest variable (Since it'll be the oldest item in the list)
            oldest = self.storage.head
            # Remove from head (the oldest item) 
            self.storage.remove_from_head()
            # Add to tail of list with the newest item
            self.storage.add_to_tail(item)
            # Also, check if the oldest item is our current item, if it is...assign to tail of the list
            if oldest == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # current item we're on assigned to item variable
        item = self.current
        # Append that item the list
        list_buffer_contents.append(item.value)
        # If the next item in the list is valid (exists)
        if item.next is not None:
            # Create a variable called next_item and assign it to that next item in the list
            next_item = item.next
            # Otherwise, assign the head item of the list to the next_item variable
        else:
            next_item = self.storage.head
        # As long as the next_item variable is not equal to our current item (Which we already appended)
        while next_item is not item:
            # Then append that item to the list
            list_buffer_contents.append(next_item.value)
            # Basically just repeat the logic working our way through all the items
            if next_item.next is not None:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        # Return the newly created list
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
