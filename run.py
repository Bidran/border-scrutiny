import time
import os
import sys
import random
from random import choice
from art import *


def typingPrint(text):
    """
    Text effect.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


"""
Various lists from which functions will pull data.
"""

first_name_men = [
    'Dmitri', 'Mikhail', 'Anton', 'Pavel', 'Andrei', 'Ivan',
    'Sergei', 'Fyodor']

first_name_women = [
    'Yelena', 'Natalia', 'Svetlana', 'Irina', 'Ekaterina',
    'Olga', 'Yulia', 'Ana']

last_name_men = [
    'Petrovich', 'Romanov', 'Kovalenko', 'Sokolov', 'Volkov',
    'Nikitin', 'Voronin', 'Romanovich',
    ]

last_name_women = [
    'Ivanova', 'Kuznetsova', 'Zhdanova', 'Popova', 'Romanovna',
    'Ilyina', 'Yegorova', 'Titova'
    ]

origin_country = [
    'Novoslavia', 'Tashkarsk', 'Dushkovia', 'Arktovia', 'Kazakhrad',
    'Bolskaya', 'Sputnikstan', 'Molotovia'
    ]

possession = [
    'Knife', 'Gun', 'Lighter', 'Cigarettes', 'Phone',
    'Chocolate', 'Crisps', 'Juice', 'Painting', 'Headphones', 'Laptop',
    'USB Stick', 'Broom', 'Rollerblades', 'Fidget Spinner', 'Lightbulb'
    ]


def makePerson():

    """
    Chooses a random choice between a man and a woman
    functions and returns the choice.
    """

    persons = [makeMan(), makeWoman()]
    chosen = random.choice(persons)
    return chosen


def makeMan():
    """
    Pulls random values from lists which will create a profile of a man.
    """
    global random_fname, random_lname, age, random_country, random_possession
    random_fname = random.choice(first_name_men)
    random_lname = random.choice(last_name_men)
    age = random.choice(range(20, 29))
    random_country = random.choice(origin_country)
    random_possession = random.choice(possession)
    return random_fname, random_lname, age, random_country, random_possession


def makeWoman():
    """
    Pulls random values from lists which will create a profile of a woman.
    """
    global random_fname, random_lname, age, random_country, random_possession
    random_fname = random.choice(first_name_women)
    random_lname = random.choice(last_name_women)
    age = random.choice(range(20, 29))
    random_country = random.choice(origin_country)
    random_possession = random.choice(possession)
    return random_fname, random_lname, age, random_country, random_possession


def newLine():
    """
    Makes space for readability.
    """
    print('\n')


"""
ANSI color values which are used troughout the code.
"""
red = '\033[0;31m'
white = "\033[0m"
green = '\033[0;32m'
yellow = '\033[0;33m'


def randomRule():
    """
    Pulls the value from lists and creates a profile of a person and saves it
    to global variables which will be used in other parts of the program.
    """
    global random_fname_chosen
    global random_lname_chosen
    global random_country_chosen
    global random_age
    random_fname_man = random.choice(first_name_men)
    random_fname_woman = random.choice(first_name_women)
    random_lname_man = random.choice(last_name_men)
    random_lname_woman = random.choice(last_name_women)
    both_first = [random_fname_man, random_fname_woman]
    random_fname_chosen = random.choice(both_first)
    if random_fname_chosen == random_fname_man:
        random_lname_chosen = random_lname_man
    else:
        random_lname_chosen = random_lname_woman
    random_country_chosen = random.choice(origin_country)
    random_age = random.choice(range(20, 29))
    newLine()
    typingPrint('Alright, the rule for today is: \n')
    typingPrint("Don't let anyone trough who has any of these: \n")
    newLine()
    typingPrint(f"First name: {red}{random_fname_chosen}{white} \n"
                f"Last name: {red}{random_lname_chosen}{white} \n"
                f"Country: {red}{random_country_chosen}{white} \n"
                f"Age: {red}{random_age} years old{white}\n")
    typingPrint(f'And remember, never let in anyone who has a {red}Knife'
                f"{white} or a {red}Gun{white}.\n")


def firstPerson():
    """
    Creates a person which is used to compare attributes with forbidden ones.
    """
    global first_person_name
    global first_person_surname
    global first_person_age
    global first_person_country
    global first_person_possession
    first_person = makePerson()
    first_person_name = first_person[0]
    first_person_surname = first_person[1]
    first_person_age = first_person[2]
    first_person_country = first_person[3]
    first_person_possession = first_person[4]
    newLine()
    print(f'{yellow} __________________________________________________'
          f'_____\n')
    print(f"|  |{white}Name: {first_person_name} {first_person_surname}"
          f"{yellow}|     |{white}Country: {first_person_country}{yellow}|\n")
    print('|------------------------------------------------------|\n')
    print(f"|  |{white}Age: {first_person_age}{yellow}|"
          f"                   |{white}"
          f"Possession: {first_person_possession}{yellow}|\n"),
    print(f'|______________________________________________________|{white}\n')


# Money value, used as score
money = 0


def beginGame():
    """
    Takes players input if they wish to proceed with the game or end it.
    """
    newLine()
    user_input = input(f'Are you ready to begin?'
                       f' ({green}yes{white}/{red}no{white}): \n')
    if user_input.lower() == 'yes':
        randomRule()
    elif user_input.lower() == 'no':
        typingPrint("Off to jail with you! \n")
        user_input_no = input(f'Did you change your mind?'
                              f'({green}yes{white}/{red}no{white}): \n')
        if user_input_no.lower() == 'yes':
            beginGame()
        elif user_input_no.lower() == 'no':
            typingPrint("Bye!")
            newLine()
            exit()
        else:
            print('Type yes or no')
            beginGame()
    else:
        print('Type yes or no')
        beginGame()


def letTrough():
    """
    Function which compares values between original random person and each
    consecutive one after which it gives {money} value accordingly.
    Called upon when replying yes.
    """
    global money
    if (random_fname_chosen == first_person_name):
        print(f"{red}You've let trough a person with forbidden first name!"
              f"\n-$20{white}")
        money = money - 20
    elif (random_lname_chosen == first_person_surname):
        print(f"{red}You've let trough a person with forbidden last name!"
              f"\n-$20{white}")
        money = money - 20
    elif (random_age == first_person_age):
        print(f"{red}You've let trough a person with forbidden age!"
              f"\n-$20{white}")
        money = money - 20
    elif (random_country_chosen == first_person_country):
        print(f"{red}You've let trough a person with forbidden origin country!"
              f"\n-$20{white}")
        money = money - 20
    elif (first_person_possession == 'Gun'
          or first_person_possession == 'Knife'):
        print(f"{red}You've let trough a person with forbidden possessions!"
              f"\n-$20{white}")
    else:
        print(f"{green}Good decision comrade!\n+$10{white}")
        money = money + 10


def dontLetTrough():
    """
    Function which compares values between original random person and each
    consecutive one after which it gives {money} value accordingly.
    Called upon when replying no.
    """
    global money
    if (random_fname_chosen == first_person_name):
        print(f"{green}You've stopped a person with forbidden first name!\n"
              f"+$30{white}")
        money = money + 30
    elif (random_lname_chosen == first_person_surname):
        print(f"{green}You've stopped a person with forbidden last name!\n"
              f"+$30{white}")
        money = money + 30
    elif (random_age == first_person_age):
        print(f"{green}You've stopped a person with forbidden age!\n"
              f"+$30{white}")
        money = money + 30
    elif (random_country_chosen == first_person_country):
        print(f"{green}You've stopped a person with forbidden origin country!"
              f"\n+$30{white}")
        money = money + 30
    elif (first_person_possession == 'Gun'
          or first_person_possession == 'Knife'):
        print(f"{green}You've stopped a person with forbidden possessions!"
              f"\n+$30{white}")
    else:
        print(f"{red}Could've let them trough!\n-$10{white}")
        money = money - 10


def borderCheck():
    """
    Input function which takes values yes and no, calling previous functions.
    """
    border_input = input(f'Do you let this person trough the border?'
                         f'({green}yes{white} or {red}no{white}): \n')
    newLine()
    if border_input.lower() == 'yes':
        letTrough()
    elif border_input.lower() == 'no':
        dontLetTrough()
    else:
        print('Type yes or no')
        borderCheck()


def introduction():
    """
    Short introduction which takes the players name with a short description.
    """
    typingPrint(f"Zdravstvuy {red}COMRADE{white}, welcome to the border"
                f". What's your name? \n")
    newLine()
    username = input("Type in your name and press return: \n")
    newLine()
    typingPrint(f"Well, officer {green}{username} {white}, seems like"
                f" you got the short end of the stick today.\nThere are enemy"
                f" spies all over the place. \n")
    typingPrint('The boss tells us each day who we can let in the motherland\n'
                'based on new information. \n')
    typingPrint('You will either earn money or lose it depending'
                ' on how well you do.\n')


def anotherDay():
    """
    Restart the game, saving your current earned money.
    """
    play_again = input(f'Your money stays with you. \nDo you want to keep'
                       f' going another day? ({green}yes{white}/{red}no'
                       f'{white}): \n')
    if play_again.lower() == 'yes':
        main()
    elif play_again.lower() == 'no':
        newLine()
        print(f'{yellow}')
        Art = text2art("Game over!")
        print(Art)
        print(f'{white}')
        newLine()
    else:
        newLine()
        print('Type yes or no')
        newLine()
        anotherDay()
        newLine()


def finalScore():
    """
    Add money to total and display to player.
    """
    if money > 1:
        print(f'{green}You have ${money}!{white}\n')
    else:
        print(f'{red}You have {money} dollars!{white}\n')
    return money


def main():
    """
    Main function which calls others when required.
    """
    beginGame()
    newLine()
    firstPerson()
    borderCheck()
    firstPerson()
    borderCheck()
    firstPerson()
    borderCheck()
    firstPerson()
    borderCheck()
    firstPerson()
    borderCheck()
    newLine()
    finalScore()
    anotherDay()
    newLine()


introduction()


main()
