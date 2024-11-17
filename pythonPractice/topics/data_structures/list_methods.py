a = [8, 10, 12, 16, 34]  # Creates list a
print(a)

# append() | Syntax: list_name.append(element)
a.append(36)  # Appends element to list
print(a)

# copy() | Syntax: list_name.copy()
b = a.copy()  # Copies list of elements to a new variable
print(b)

# clear() | Syntax: list_name.clear()
a.clear()  # Clears the elements of a list
print(a)

# copy() | Syntax: list_name.copy()
a = b.copy()
print(a)

# count() | Syntax: list_name.count(element)
print(a.count(36))

# extend() | Syntax: list_name.extend(iterable)
a.extend([99, 100])  # Adds elements of another list
print(a)

# index | Syntax: list_name.index(element)
print(a.index(99))  # Print the index of the item "99"

# insert() | Syntax: list_name.insert(index, element)
a.insert(1, 2)

# pop() | Syntax: list_name.pop(index)
a.pop()
print(a)

# remove() | Syntax: list_name.remove(element)
# Remove the first occurrence of a list
a.remove(2)
print(a)

# reverse() | Syntax: list_name.reverse()
# Reverse the order of the elements in the list
a.reverse()
print(a)

# sort() | Syntax: list_name.sort()
# Sort in ascending order
a.sort()
print(a)