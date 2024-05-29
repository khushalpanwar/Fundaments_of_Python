""" 
Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.

"""

def get_first_and_last_two_chars(input_string):
    if len(input_string) < 2:
        return ""  # Return empty string if the input length is less than 2
    else:
        return input_string[:2] + input_string[-2:]  # Concatenate the first two and last two characters

# Example usage:
input_str = "python"
result = get_first_and_last_two_chars(input_str)
print("Result:", result)
