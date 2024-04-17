# Write a python program to count character of a string 

word = " PythonPrograming"

character_list = []

character_counter = {}  # count each character

for c in word :
    character_list.append(c)
    
#print(character_list)

for c in character_list:
    if c in character_counter:
        character_counter[c] += 1
    else:
        character_counter[c] = 1
        
print(character_counter)