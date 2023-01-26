import random

options = ('Piedra', 'Papel', 'Tijera')

user_option = input('Piedra, Papel o Tijera => ')
user_option = user_option.title()

if not user_option in options:
  print('Esa opción no es valida')

computer_option = random.choice(options)

print(f'User option => {user_option}')
print(f'Computer option => {computer_option}')

if user_option == computer_option:
  print("Empate")
elif user_option == 'Piedra':
  if computer_option == 'Tijera':
    print(
      f"El usuario tiene {user_option} y la maquina tiene {computer_option}")
    print(f"por ende {user_option} gana a {computer_option}")
    print("User gana!!!")
  else:
    print(f"{computer_option} gana a {user_option}")
    print("Maquina gano!!!")

elif user_option == 'Papel':
  if computer_option == 'Piedra':
    print(
      f"El usuario tiene {user_option} y la maquina tiene {computer_option}")
    print(f"por ende {user_option} gana a {computer_option}")
    print("User gana!!!")
  else:
    print(f"{computer_option} gana a {user_option}")
    print("Maquina gano!!!")

elif user_option == 'Tijera':
  if computer_option == 'Papel':
    print(
      f"El usuario tiene {user_option} y la maquina tiene {computer_option}")
    print(f"por ende {user_option} gana a {computer_option}")
    print("User gana!!!")
  else:
    print(f"{computer_option} gana a {user_option}")
    print("Maquina gano!!!")
