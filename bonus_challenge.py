import operator # Imports operator module to sort dictionary.

diction = {} # Creates empty dictionary.
spaces = " " # Will contain discared spaces.

user_input = input("Please enter a string to be counted: ") # Prompts user for input.

for letter in user_input: # Loops through each letter in user input.
    if letter == " ": # Checks if letter is in space.
        spaces += " "
    elif letter in diction: # If letter is in dictionary...
        diction[letter] += 1 # We increment the key's value by 1.
    else:
        diction[letter] = 1 # We assign 1 to the current value of the said key.

# Sorts dictionary in ascending order.
sorted_diction = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)

# Prints the first three items in the sorted dictionary.
print(sorted_diction[0])
print(sorted_diction[1])
print(sorted_diction[2])