lists_are = [
    "Ordered",
    "Zero-based",
    "Mutable",
    "Heterogeneous",
    "Growable and dynamic",
    "Nestable",
    "Iterable",
    "Sliceable",
    "Combinable",
    "Copyable"
]

print(f" Lists are: {lists_are}")

heterogenous = [42, "apple", True, {"name": "Jared Batchelor"}, (1, 2, 3), [3.14, 2.78]]

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]

print(colors)

print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

inventory = [
    {"product": "phone", "price": 1000, "quantity": 10},
    {"product": "laptop", "price": 1500, "quantity": 5},
    {"product": "tablet", "price": 500, "quantity": 5}
]

functions = [print, len, range, type, enumerate]

empty = []

list_constructor_1 = list((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(list_constructor_1)

list_constructor_2 = list({"circle", "square", "triangle", "rectangle", "pentagon"})
print(list_constructor_2)

list_constructor_3 = list({"name": "John", "age": 30, "city": "New York"}.items())
print(list_constructor_3)

list_constructor_4 = list("Pythonista")
print(list_constructor_4)

def fibonacci_generator(stop):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_number = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_number
        
list(fibonacci_generator(10))