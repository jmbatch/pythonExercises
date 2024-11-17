# Define an integer
x = 10  # 'x' is an integer with a value of 10

# Change the value of an integer by assigning a new value
x = 15 # 'x' has a new value of 15

# Arithmetic operations
y = x + 5     # Addition: y = 20
z = x - 5     # Subtraction: z = 10
a = x * 2     # Multiplication: a = 30
b = x / 2     # Division: b = 7.5 (this is a float, not an integer)
c = x // 2    # Integer division (This drops the decimal): c = 7
d = x % 3     # Modulo: Returns the remainder
e = +x        # Sets integer to positive if x is negative. Unchanged if already positive
f = -x        # x Negated: -15
g = abs(x)    # Returns absolute value or magnitude of x
h = int(x)    # x converted to integer
i = float(x)  # x converted to float
j = divmod(x, y)  # the pair (x // y, x % y)
k = pow(x, y)  # x to the power of y
l = x ** y     # x to the power of y  

# Use integers to control the number of loop iterations
for i in range(x):  # Iterates 15 times by using values 0 to 14
    print(i)
    
# You can use integers to index lists
my_list = [10, 20, 30, 40, 50]
first_item = my_list[0]

# Integers can be defined with binary, octal, and hexidecimal notation
binary_int = 0b1010  # Binary for 10 in decimal
octal_int = 0o12     # Octal for 10 in decimal
hex_int = 0xA        # Hexadecimal for 10 in decimal

# Using integers in a function
def add_five(num):
    return num + 5  # Adds 5 to the input integer and returns the result

result = add_five(x)  # Call the function with x (x = 15). 'result' will be 20


#  Methods
#  int.bit_length()
n = -37
binary_n = bin(n)  # Binary for n: '-0b100101'
bit_length_n = n.bit_length()  # bit length of n

# int.bit_length() is the equivalent of: 
def bit_length(self):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)  

# int.bit_count()
n = 19
binary_n = bin(n)  # Binary for n: '0b10011'
bit_count_n = n.bit_count()  # number of ones in the binary absolute value of n

# int.bit_count() is the equivalent of:
def bit_count(self):
    return bin(self).count("1")

# int.to_bytes(length=1, byteorder='big', *, signed=False)
# Return an array of bytes representing an integer.
n = 1000
n_bytes = n.to_bytes((n.bit_length() + 7) // 8, byteorder='little')

# int.from_bytes()
n_unsigned = int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)  # → 64512 (positive integer)
n_signed = int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)   # → -1024 (negative integer)