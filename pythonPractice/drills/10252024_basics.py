# 1. List Comprehension Basics
# Goal: Create a list using list comprehension that contains the squares of even numbers from 0 to 20.
# Expected Result: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
even_squares = [val ** 2 for val in range(0, 21) if val % 2 == 0]
print(even_squares)

# Refined
even_squares = [val ** 2 for val in range(0, 21, 2)]
print(even_squares)


# 2. Dictionary Creation with Conditional Values
# Goal: Create a dictionary where the keys are numbers from 1 to 10 and the values are "even" if the number is even and "odd" if the number is odd.
# Expected Result: {1: "odd", 2: "even", 3: "odd", ..., 10: "even"}
even_odd_dict = {}
for i in range(1, 11):
    if i % 2 == 0:
        even_odd_dict[i] = "even"
    else:
        even_odd_dict[i] = "odd"
print(even_odd_dict)

even_odd_dict = {i: "even" if i % 2 == 0 else "odd" for i in range(1, 11)}
print(even_odd_dict)


# 3. Linked List Basics
# Goal: Implement a basic singly linked list with Node and LinkedList classes. Include methods to add a new node to the end and print all nodes.
# Expected Result: After adding 1, 2, 3 to the list, printing the list should display 1 -> 2 -> 3.




# 4. Set Operations
# Goal: Create two sets, A and B. Populate A with numbers 1 to 5, and B with numbers 3 to 7. Then, compute and print the union, intersection, and difference of the two sets.
# Expected Result:
# Union: {1, 2, 3, 4, 5, 6, 7}
# Intersection: {3, 4, 5}
# Difference (A - B): {1, 2}




# 5. Basic Queue Operations
# Goal: Implement a queue using a list. Include functions to enqueue (add) and dequeue (remove) items. Start with an empty queue, enqueue numbers 1 to 3, and then dequeue one item.
# Expected Result: After dequeuing, the queue should contain [2, 3].




# 6. Dictionary Comprehension with String Manipulation
# Goal: Given a list of names, ["Alice", "Bob", "Catherine", "David"], create a dictionary comprehension where the keys are names and the values are the length of each name.
# Expected Result: {"Alice": 5, "Bob": 3, "Catherine": 9, "David": 5}




# 7. Stack Operations
# Goal: Create a stack using a list and implement push and pop operations. Push the numbers 1, 2, and 3 onto the stack, then pop one item.
# Expected Result: After popping, the stack should contain [1, 2].




# 8. List Filtering with List Comprehension
# Goal: Use list comprehension to filter out all negative numbers from a list numbers = [-5, 3, -1, 101, -50, 10].
# Expected Result: [3, 101, 10]




# 9. Tuple Unpacking
# Goal: Given a tuple coordinates = (10, 20, 30), unpack the tuple into three separate variables x, y, and z, and print them in the format: "x: 10, y: 20, z: 30".
# Expected Result: Print statement output should be "x: 10, y: 20, z: 30".




# 10. Finding the Maximum in a List Using a Loop
# Goal: Without using the max() function, write a loop to find the maximum number in a list of integers, numbers = [23, 1, 45, 34, 78, 15].
# Expected Result: 78