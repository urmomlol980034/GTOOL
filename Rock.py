#1 = rock 
#2 = paper
#3 = sizzors
# defining functions
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')
#staring the program
while 1 < 2:
  #options
  clear()
  from random import randint
  option = input('Choose rock = r \nChoose paper = p\nOr scizzors = s\nQuit = q\n> ')
  pcChoice = randint(1,3)
  if pcChoice == 1 and option == 'p':
    print('I chose rock')
    print('Good job you won!')

  if option == 'r' and pcChoice == 1:
    print('We tied with rock!')

  if option == 's' and pcChoice == 1:
    print('I chose rock I won. Yay!')

  if pcChoice == 2 and option == 'r':
    print('I chose Paper I win. Yay!')
  
  if pcChoice == 2 and option == 'p':
    print('We tie!')
  
  if pcChoice == 2 and option == 's':
    print('Good job! you chose sizzors you win!')

  if pcChoice == 3 and option == 'r':
    print('Good job! you chose rock You win!')
  
  if pcChoice == 3 and option == 'p':
    print('Yay i chose sizzors I win!')
  
  if pcChoice == 3 and option == 's':
    print('We both tie with sizzos')
  # quiting code
  if option == 'q':
    quit()
  input('|:PRESS ENTER WHEN DONE:|')
  clear()
