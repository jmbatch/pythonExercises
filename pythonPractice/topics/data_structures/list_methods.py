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

# Syntax: newList = [ expression(element) for element in oldList if condition ] 
# Parameter:
#   expression: Represents the operation you want to execute on every item within the iterable.
#   element: The term “variable” refers to each value taken from the iterable.
#   iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
#   condition: (Optional) A filter helps decide whether or not an element should be added to the new list.

# List comprehension with expression (multiplication)
numbers = [1, 2, 3, 4, 5, 6, 7, 8,]
doubled = [x * 2 for x in numbers]
print(doubled)


# In this example, we are assigning 1, 2, and 3 to the list and 
#   we are printing the list using List Comprehension.
# Using list comprehension to iterate through loop 
List = [character for character in [1,2,3]]
print(List)


# In this example, we are printing the even numbers from 0 to 10 using List Comprehension.
even_list = [x for x in range(11) if x % 2 == 0]
print(even_list)