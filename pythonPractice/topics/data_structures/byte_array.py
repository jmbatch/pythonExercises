# bytearray() method returns a bytearray object in Python which is an array of given bytes. It gives a mutable sequence of integers in the range 0 <= x < 256. 

# Syntax of bytearray() Function in Python
# Python bytearray() function has the following syntax:

# Syntax: bytearray(source, encoding, errors)

# Parameters:

# source[optional]: Initializes the array of bytes
# encoding[optional]: Encoding of the string
# errors[optional]: Takes action when encoding fails
# Returns: Returns an array of bytes of the given size.

# source parameter can be used to initialize the array in few different ways. Let’s discuss each one by one with help of examples. 

# Example 1: Reading and modifying binary data
data = bytearray(b"Hello World!")
data[6:11] = b"Python"
print(data)  # Output: bytearray(b'Hello Python!')

# Example 2: Constructing a network packet
packet = bytearray(10)
packet[0] = 0xFF  # Setting the first byte
packet[1] = 0x10  # Setting the second byte
print(packet)  # Output: bytearray(b'\xff\x10\x00\x00\x00\x00\x00\x00\x00\x00')

# Example 3: Encoding and decoding text
text = "Hello World!"
encoded = bytearray(text, 'utf-8')
print(encoded)  # Output: bytearray(b'Hello World!')
decoded = encoded.decode('utf-8')
print(decoded)  # Output: Hello World!