
contacts = {
    'number': 4,
    'students':
    [
        {'name':'Sara Morales', 'email':'smorales@aol.com'},
        {'name':'Ruperto Veloz', 'email':'rveloz@aol.com'},
        {'name':'Juan Morcillo', 'email':'jmorcillo@aol.com'},
        {'name':'Paula Brijan', 'email':'pbrijan@aol.com'}
    ]
}

#let's get only the email addresses
print('Student emails:')
for student in contacts['students']:
    print(student['email'])
    