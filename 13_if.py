"""if True:
  print ('Debería ejecutarse')

if False:
  print ('Nunca se ejecuta')

pet = input('¿Cuál es tu mascota favorita?')

if pet == 'perro':
  print ('Nice dude')

if pet == 'gato':
  print ('dont worry dude')

stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print ("El stock es correcto ingresa en las caractericas")
else:
  print ("No cumple con las caracteristicas, sobre stock")"""

number = int(input('Ingresa un numero => '))
result = number % 2
if (result == 0):
  print ('par')
else:
  print ('No par')