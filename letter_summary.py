# Prints a dictionary containing the tally of how many 
# times each letter in the alphabet was used in the word.

diction = {} #Creates an empty dictionary.

user_input = input("Please enter a string: ") # Asks for user input.

for letter in user_input: # Loops through letters in user input.
    if letter in diction: # Checks to see if letter in user input is inside empty dictionary.
        diction[letter] += 1 # If it is we increment the key's value by 1.
    else: # Otherwise we assign 1 to any other letter passed.
        diction[letter] = 1

print(diction) # Prints the result.
