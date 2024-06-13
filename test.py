from random import randint, choice as random_element  # alias
from termcolor import cprint
from emoji import emojize
# from decouple import config

print(randint(1, 6))
print(random_element(['apple', 'pear', 'orange', 'banana']))


cprint("Hello, World!", "green", "on_red")
print(emojize('Python is :thumbs_up:'))
print('Hello from CMD!')