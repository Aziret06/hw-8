import logic
from decouple import config

default_bet = config('INIT_CAPITAL')
my_cash = int(config('MY_MONEY', default=1000))
attempts = config('ATTEMPTS')

while my_cash > 0:
    answer = input("Would you like to play ? (y/n): ").lower()
    if answer == 'n':
        print(f"That is your cash: {my_cash}")
        break
    elif answer == 'y':
        my_bet = int(input('How much money would you bet: '))
        if my_bet > my_cash or my_bet < 0:
            print('You should bet from 1 to 1000')
            continue
        chosen_number = int(input('What number would you like to bet on(from 1 to 10):' ))
        if chosen_number > 10 or chosen_number < 1:
            print('You must enter a number between 1 and 10')
            continue
        if chosen_number == logic.correct_number:
            print('Congratulations!')
            my_cash += my_bet * 2
        else:
            print('You lose')
            my_cash -= my_bet
    else:
        print("You must enter y or n")
