# Truth Value Testing
test = "test"
def check_if_true(x):
    if x:
        print("This is true.")
    else:
        print("This is false.")

name = "Jared"
age = 36
empty_list = []
not_empty_list = [1, 2, 3]
check_if_true(name)  # Output: True
check_if_true(age)  # Output: True
check_if_true(empty_list)  # Output: False
check_if_true(not_empty_list)  # Output: True

# Boolean operations - and, or, not
# Logical AND
x = 10
y = 5
result = (x > 0) and (y < 10)
print(result)  # Output: True

# Logical OR
is_sunny = True
is_warm = False
beach_day = is_sunny or is_warm
print(beach_day)  # Output: True

# Logical NOT
has_key = False
door_locked = not has_key
print(door_locked)  # Output: True