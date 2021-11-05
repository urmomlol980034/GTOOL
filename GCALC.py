# defining functions
from colorama import Style
from colorama import Fore
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

# Starting the functions
while 1 < 2:
  # menu
  clear()
  print('+========================+\n|> Created by: GavinRepls|\n|> OFFICIAL: GCALC LITE  |\n+========================+')
  print('\nMenu:')

  Option = eval(input('1.) Free Equation\n2.) Square Root\n3.) Cube Root\n4.) Even/Odd Check\n5.) Timer/Stopwatch\n6.) QUIT = 6 \n |>==: '))
  #options
  if Option == 1:
    clear()
    equ = eval(input('OPTION 1: Free Equation(1)\nEnter Your Equation here\n> '))
    print('Your Answer Is:',equ)
    input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
    clear()
  if Option == 2:
    clear()
    from math import sqrt
    square = eval(input('OPTION 2: Square Root(2)\nEnter Your Number That You Want To See The Square Root Of\n> '))
    equ = sqrt(square)
    print('The Square root of your number',square,'is:',equ)
    input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
    clear()
  
  if Option == 3:
    clear()
    cube = eval(input('OPTION 3: Cube Root(3)\nEnter The Number You Want To See The Cube Root Of\n> '))
    equ = cube**(1. / 3)
    print('The Cube root of your number',cube,'is:',equ)
    input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
    clear()
  
  if Option == 4:
    clear()
    mod = eval(input('OPTION 4: Even/Odd Check(4)\nEnter The Number You Want To See If Its Even Or Odd\n> '))

    if mod % 2 == 0:
      print('Your number',mod,'is even')

    if mod % 2 == 1:
      print('Your number',mod,'Is odd')
    input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
    clear()
  
  if Option == 5:
    clear()
    TorS = eval(input('OPTION 5: Stopwatch/Timer\n1.) Timer\n2.) Stopwatch\n> '))
    if TorS == 1:
      import time
      def countdown(t):
    
        while t:
          mins, secs = divmod(t, 60)
          timer = '{:02d}:{:02d}'.format(mins, secs)
          print(timer, end="\r")
          time.sleep(1)
          t -= 1

      t = input("Enter the time in seconds: ")
      countdown(int(t))
      print('TIMES UP!!')
      input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
      clear()

    if TorS == 2:
      from os import system, name
      from time import sleep

      def clear():
          if name == 'nt':
              _ = system('cls')
          else:
            _ = system('clear')

      hour = 0
      minute = 0
      seconds = 0
      input('Press enter to start')
      while True:
        print('------------\n',hour,':',minute,':',seconds,'\n------------\nCTRL+C: To Quit')
        seconds += 1
        sleep(1)
        clear()
        if seconds == 60:
          seconds = 0
          minute += 1
  
        if minute == 60:
          minute = 0
          hour += 1
  # excreted        
  if Option == 6:
    quit()
  if Option < 1:
    print(f'{Fore.RED}ERROR MESSAGE: Please enter a valid number{Style.RESET_ALL}')
    input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
    clear()
  if Option > 6:
    print(f'{Fore.RED}ERROR MESSAGE: Please enter a valid number{Style.RESET_ALL}')
    input(' ***********************\n|:PRESS ENTER WHEN DONE:|\n ***********************')
    clear()
