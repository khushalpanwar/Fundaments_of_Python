"""

Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.



"""

def replace_not_poor(sentence):
    index_not = sentence.find('not')
    index_poor = sentence.find('poor')

    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        return sentence.replace(sentence[index_not:index_poor + 4], 'good')
    else:
        return sentence


input_str = input("Enter your string here : ")
result = replace_not_poor(input_str)
print("Result:", result)
