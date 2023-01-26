print(not True)
print(not False)

# and
print ('not and')
print ('not True and True =>', not (True and True))
print ('not True and False =>', not (True and False))
print ('not False and True', not (False and True))
print ('not False and False =>', not (False and False))

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print (not (stock >= 100 and stock <= 1000))

# or
print ('not or')
print ('not True or True =>', not (True or True))
print ('not True or False =>', not (True or False))
print ('not False or True', not (False or True))
print ('not False or False =>', not (False or False))

role = input('Digita el rol => ')
print (not (role == 'admin' or role == 'seller'))