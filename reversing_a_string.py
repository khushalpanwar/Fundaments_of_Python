""" 
Write a Python function to reverses a string if its length is a multiple of 4.
"""

def reverse_string_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]  # Reversing the string using slicing
    else:
        return input_string

# Example usage:
input_str = "abcdefgh"
result = reverse_string_if_multiple_of_4(input_str)
print("Result:", result)
