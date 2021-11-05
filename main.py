from colorama import Fore
from colorama import Style
#functions
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')
#starting the Tool
while 1 < 2:
  #menu 
  print(f'==========================\n|> Created by: {Fore.GREEN}GavinRepls{Style.RESET_ALL}|\n|> Oficial: {Fore.LIGHTCYAN_EX}GTOOL{Style.RESET_ALL}{Fore.LIGHTRED_EX}©{Style.RESET_ALL}       |\n==========================\nNOW WITH {Fore.RED}C{Style.RESET_ALL}{Fore.GREEN}O{Style.RESET_ALL}{Fore.CYAN}L{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}O{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}R{Style.RESET_ALL}{Fore.LIGHTCYAN_EX}!{Style.RESET_ALL}\nUSE: Check the READ.md file to see how to use.')
  from logo import logo
  
  print('\nMenu: ')
  print('GCALC LITE = 1\nRock Paper Sizzors = 2\nDATA SCRAPER HACK = 3\nMORE HACKS COMING SOON!',end = '')
  print("""                      
                                 ____          
                                !###!               
                               !#####                  
                              !###|'###                
                               ---   !#!              
                                       ##            
                                        !#!         
                                          ##       
                                           !#! 
                                                
  """,end = '') 
  Tool = eval(input('|> '))
  #options
  if Tool == 1:
    from GCALC import GCALC
    exec(GCALC.py)

  if Tool == 2:
    from Rock import Rock
    exec(Rock.py)

  if Tool == 3:
    from SCRAPER import SCRAPER
    exec(SCRAPER.py)
  # excreted
  if Tool > 3:
    print(f'{Fore.RED}ERROR MESSAGE: Please Enter A Valid Function.{Style.RESET_ALL}')
    input('|:PRESS ENTER WHEN DONE:|') 
    clear()

  if Tool < 1:
    print(f'{Fore.RED}ERROR MESSAGE: Please Enter A Valid Function.{Style.RESET_ALL}')   
    input('|:PRESS ENTER WHEN DONE:|')
    clear()
