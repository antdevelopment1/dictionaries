# Prints a dictionary containing the tally of how many 
# times each word in the alphabet was used in the text.

# Prompts user for input and splits the result into indiviual words.
user_input = input("Please provide a string to be counted by words: ").split(" ")

diction = {} # Creates an empty dictionary.

for word in user_input: # Loops through words in user input.
    if word in diction: # Checks to see if word is already inside dictionary.
        diction[word] += 1 # If it is, we increment by.
    else: # Otherwise we assign 1 to any words not repeated more than once.
        diction[word] = 1

print(diction) # Print the modified dictionary.
