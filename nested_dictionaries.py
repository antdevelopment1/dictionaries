# Dictionary with nested dictionaries and key value pairs.
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit['email']) # Prints email address of Ramit.
print(ramit['interests'][0]) # Gets the first of Ramit's interests.
print(ramit['friends'][0]['email']) # Gets the email address of Jasmine.
print(ramit['friends'][1]['interests'][1]) # Write a python expression that gets the second of Jan's two interests.