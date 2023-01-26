import random

options = ('Piedra', 'Papel', 'Tijera')

rounds = 1
computer_wins = 0
user_wins = 0

while True:

  print('*' * 10)
  print(f'Round {rounds}')
  print('*' * 10)

  print("*"*4, "Wins", "*"*4)
  print(f"wins de maquina = {computer_wins}")
  print(f"wins de usuario = {user_wins}")
  print("*"*4, "Wins", "*"*4)
  
  user_option = input('Piedra, Papel o Tijera => ')
  user_option = user_option.title()
  
  if not user_option in options:
    print('Esa opción no es valida')
    continue
  
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
      user_wins += 1
    else:
      print(f"{computer_option} gana a {user_option}")
      print("Maquina gano!!!")
      computer_wins +=1
  elif user_option == 'Papel':
    if computer_option == 'Piedra':
      print(
        f"El usuario tiene {user_option} y la maquina tiene {computer_option}")
      print(f"por ende {user_option} gana a {computer_option}")
      print("User gana!!!")
      user_wins += 1
    else:
      print(f"{computer_option} gana a {user_option}")
      print("Maquina gano!!!")
      computer_wins +=1
  elif user_option == 'Tijera':
    if computer_option == 'Papel':
      print(
        f"El usuario tiene {user_option} y la maquina tiene {computer_option}")
      print(f"por ende {user_option} gana a {computer_option}")
      print("User gana!!!")
      user_wins += 1
    else:
      print(f"{computer_option} gana a {user_option}")
      print("Maquina gano!!!")
      computer_wins +=1

  if computer_wins == 2:
    print('El ganador es la computadora')
    print("*"*4, "Wins", "*"*4)
    print(f"wins de maquina = {computer_wins}")
    print(f"wins de usuario = {user_wins}")
    print("*"*4, "Wins", "*"*4)
    break
    
  if user_wins == 2:
    print("Has ganado usuario congrats")
    print("*"*4, "Wins", "*"*4)
    print(f"wins de maquina = {computer_wins}")
    print(f"wins de usuario = {user_wins}")
    print("*"*4, "Wins", "*"*4)
    break
  
  rounds += 1