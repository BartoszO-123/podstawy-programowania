person = {
    'name': 'Marek',
    'surname': 'Banach',
    'age': 25,
    'hobby': ['swimming','excursions'],
    'married': True,
    'phone':{'landline':'123444321','mobile':'777888999'}
}

# Displays name
print(f'Name: {person['name']}')
# Displays hobby
print(f'Hobby: {person['hobby']}')
# Displays the entire contents of the dictionary
print(f'\nEntire contents of the dictionary: {person}\n')
# Changes surname to 'Nowak'
person['surname'] = 'Nowak'
# Changes person's marriage status
person['married'] = False
# Adds gender: 'male'
person['gender'] = 'male'
# Adds a new hobby: 'bicycle'
person['hobby'].append('bicycle')
# Adds work phone to existing phones: '313131444'
person['phone']['work'] = '313131444'
# Displays the entire contents of the dictionary (iterate over dictionary items)
for key, value in person.items():
    print(f'{key} : {value}')
    