
from termcolor import colored

#uzytkownik podaje wysokosc jednego trojkata  oraz ilosc poziomow choinki
w = int(input("Proszę podać wysokość trójkąta w choince: "))
poz = int(input("Proszę podać ilość poziomów choinki: "))

#wyliczamy jaka bedzie maks szerokosc choinki oznaczona jako mx_szer
mx_szer = 2 * w * poz - 1

# Rysujemy poziomy choinki
for j in range(poz):
    for i in range(w + j):
        print(colored(' ' * ((mx_szer-(2 * i + 1)) // 2) + '#' * (2 * i + 1), 'green'))

#rysujemy pien choinki
if w > 3 | poz > 3:
   for i in range(1,3):
     print(colored(' ' * (mx_szer//2) + '##','black'))
else:
  print(colored(' ' * (mx_szer//2) + '#','black'))