#CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) #Appends=Insertar numeros al final de la lista
print(numbers)

numbers.insert(0,'hola') #insert = insertar valores en una posición.
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2') #index = Revisar en que posición esta 'X' elemento
new_list[index] = 'todo changes'
print(new_list)

new_list.remove('todo 1') #Remove = sirve para remover un elemento de la lista
print(new_list)

new_list.pop()#Pop: Sirve para remover el ultimo elemento de la lista
print(new_list)

new_list.pop(0)#pop(x): sirve para remover el elemento en alguna posición
print(new_list)

new_list.reverse() #Invertir la lista
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort()#sort = Ordenar la lista
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)