import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Runtime of the double for loop solution was O(n^2)
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
    # for name_2 in names_2:
        # if name_1 == name_2:
            # duplicates.append(name_1)

new_list = BinarySearchTree('')  # Init a BST called new_list, we will store strings(names) in it.

for second_name_list in names_2:  # Loop over names_2 and insert all the names in the BST
    new_list.insert(second_name_list)

for first_name_list in names_1:   # Loop over names_1
    # check if the BST contains any names from first_name_list
    if new_list.contains(first_name_list):
        # If so, append those names to the duplicates list
        duplicates.append(first_name_list)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
