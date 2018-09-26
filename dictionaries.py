# Dictionary containing key value pairs.
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth']) # Print the value of Elizabeth.

phonebook_dict['Kareem'] = '938-489-1234' # Adds and prints a new key value entry named Kareem.
print(phonebook_dict["Kareem"])

del phonebook_dict['Alice'] # Deletes a key value pair named Alice and prints the result.
print(phonebook_dict)

phonebook_dict["Bob"] = '968-345-2345' # Changes a key's valiue to a different number.
print(phonebook_dict["Bob"])

for phone_numbers in phonebook_dict.values(): # Loops through the values in the dictionary and prints the values of the dictionary.
    print(phone_numbers)

