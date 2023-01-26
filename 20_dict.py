person = {
  'name': 'Julian',
  'last_name': 'Vidal',
  'langs': ['python', 'JavaScript'],
  'age': 20
}

#print(person)

person['name'] = 'Juli'
person['age'] -= 1
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age') #En pop para dict se tiene que agregar el valor a elminar.

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())