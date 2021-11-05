# defining functions and importing them
from colorama import Fore
from colorama import Style
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')
# libraries
import urllib.request
from bs4 import BeautifulSoup
import csv

clear()
# starting the code
print('AFTER DATA EXTRACTION IS DONE GO TO YOUR NAMED FILE AND OPEN THE txt FILE YOU NAMED(YOUR DATA WILL BE THIER)')
filename = input('What do you want your file name to be?\n|>')
print(f'{Fore.GREEN}-COMPLETED-{Style.RESET_ALL}')
sleep(2)
clear()
print('Dont forget the https://\nEXAMPLE: https://example.com\nEnter your url here')
url = input('\n|> ')
# Fetching the html
request = urllib.request.Request(url)
content = urllib.request.urlopen(request)
# Parsing the html 
parse = BeautifulSoup(content, 'html.parser')

text1 = parse.find_all('h3', attrs={'class': 'css-5pe77f'})
text2 = parse.find_all('p', attrs={'class': 'css-hjukut'})
# writing the you grab
with open(filename, 'a') as txt_file:
  writer = csv.writer(txt_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Title','Author'])
  for col1,col2 in zip(text1, text2):
    writer.writerow([col1.get_text().strip(), col2.get_text().strip()])
x = print(f'{Fore.GREEN}-EXTRACTION COMPLETE-{Style.RESET_ALL}')
input('|:PRESS ENTER WHEN DONE:|')
quit()
