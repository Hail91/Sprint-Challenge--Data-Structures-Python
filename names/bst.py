class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes for us to call insert on them.
        if value < self.value:
            # check if self.left node exists
            if self.left:
                # Call insert method on the left side passing in the value
                self.left.insert(value)
            else:
                # If nothing exists on the left side
                # Then assign the value to the left side recursively,
                # We use recursion to cascade through the tree until we find an empty spot.
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: # If target is found, return True
            return True
        else:
            if target > self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
            else:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        while(node.right is not None):
            node = node.right
        return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        node = self
        cb(node.value)
        # Need to iterate over all the nodes in the tree
        if node.left:
            # Execute the callback function on each node we hit 
            node.left.for_each(cb)
        if node.right:
            # Execute the callback function on each node we hit 
            node.right.for_each(cb)