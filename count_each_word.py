 #Write a Python program to count the occurrences of each word in a given sentence
 
 
 # Dictionary = 


sentence = "This is python language and python is a most popular programing language "

# convert sentence into word list

word_list = sentence.split()

# print(word_list)


word_counter = {}  # dictionary to contain each word count

""" 
this : 1
is : 2
python : 2
"""

for word in word_list:
    if word in word_counter:
        word_counter[word] += 1
    else:
        # {java : }
        # key = value
        word_counter[word] = 1
        # {java : 1}
        
print(word_counter)

