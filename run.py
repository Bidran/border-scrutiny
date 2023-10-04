import time,os,sys,random
from random import choice

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)


first_name_men = [
    'Dmitri','Mikhail','Anton','Pavel','Andrei','Ivan',
    'Sergei','Fyodor'
    ]

first_name_women = [
    'Yelena','Natalia','Svetlana','Irina','Ekaterina',
    'Olga','Yulia','Ana'
    ]

last_name_men = [
    'Petrovich','Romanov','Kovalenko','Sokolov','Volkov',
    'Nikitin','Voronin','Romanovich',
    ]

last_name_women = [
    'Ivanova','Kuznetsova','Zhdanova','Popova','Romanovna',
    'Ilyina','Yegorova','Titova'
    ]

origin_country = [
    'Novoslavia','Tashkarsk','Dushkovia','Arktovia','Kazakhrad',
    'Bolskaya','Sputnikstan','Molotovia'
    ] 

possession = [
    'Knife','Gun','Lighter','Cigarettes','Phone',
    'Chocolate','Crisps','Juice','Painting','Headphones','Laptop',
    'USB Stick', 'Broom', 'Rollerblades','Fidget Spinner','Lightbulb'
    ]

def makePerson():
    persons = [makeMan(), makeWoman()]
    chosen = random.choice(persons)
    return chosen
    

def makeMan():
    global random_fname,random_lname,age,random_country,random_possession
    random_fname = random.choice(first_name_men)
    random_lname = random.choice(last_name_men)
    age = random.choice(range(10,100))
    random_country = random.choice(origin_country)
    random_possession = random.choice(possession)
    return random_fname,random_lname,age,random_country,random_possession
    
def makeWoman():
    global random_fname,random_lname,age,random_country,random_possession
    random_fname = random.choice(first_name_women)
    random_lname = random.choice(last_name_women)
    age = random.choice(range(10,100))
    random_country = random.choice(origin_country)
    random_possession = random.choice(possession)
    return random_fname,random_lname,age,random_country,random_possession
    


def newLine():
    """
    Makes space for readability
    """
    print('\n')

red = '\033[1;31;40m'
white = '\033[1;37;40m'
green = '\033[1;32;40m'
yellow = '\033[1;33;40m'

def randomRule():
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
    random_age = random.choice(range(10,100))
    newLine()
    typingPrint('Alright, the rule for today is: \n')
    typingPrint("Don't let anyone trough who has any of these: \n")
    newLine()
    typingPrint(f"First name: {red}{random_fname_chosen}{white} \nLast name: {red}{random_lname_chosen}{white} \nCountry: {red}{random_country_chosen}{white} \nAge: {red}{random_age} years old{white}\n")
    typingPrint(f'And remember, never let in anyone who has a {red}Knife{white} or a {red}Gun{white}.\n')
    return random_fname_chosen
    return random_lname_chosen
    return random_country_chosen
    return random_age

def firstPerson():
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
    print(f'{yellow} _______________________________________________________\n')
    print(f"|  |{white}Name: {first_person_name} {first_person_surname}{yellow}|     |{white}Country: {first_person_country}{yellow}|\n")
    print('|------------------------------------------------------|\n')
    print(f"|  |{white}Age: {first_person_age}{yellow}|                   |{white}Possession: {first_person_possession}{yellow}|\n"),
    print(f'|______________________________________________________|{white}\n')

money = 0

def beginGame():
    """
    Takes players input if he wishes to proceed with the game.
    """
    newLine()
    user_input = input(f'Are you ready to begin? ({green}yes{white}/{red}no{white}): \n')
    if user_input.lower() == 'yes':
        randomRule()
    elif user_input.lower() == 'no':
        typingPrint("Off to jail with you! \n")
        user_input_no = input(f'Did you change your mind? ({green}yes{white}/{red}no{white}): \n')
        if user_input_no.lower() == 'yes':
            beginGame()
        elif user_input_no.lower() == 'no':
            typingPrint("Bye!")
        else:
            print('Type yes or no')
            beginGame()
    else:
        print('Type yes or no')
        beginGame()

def letTrough():
    global money
    if (random_fname_chosen == first_person_name):
        print(f"{red}You've let trough a person with forbidden first name!\n-$20{white}")
        money = money - 20
    elif (random_lname_chosen == first_person_surname):
        print(f"{red}You've let trough a person with forbidden last name!\n-$20{white}")
        money = money - 20
    elif (random_age == first_person_age):
        print(f"{red}You've let trough a person with forbidden age!\n-$20{white}")
        money = money - 20
    elif (random_country_chosen == first_person_country):
        print(f"{red}You've let trough a person with forbidden origin country!\n-$20{white}")
        money = money - 20
    elif (first_person_possession == 'Gun' or first_person_possession == 'Knife'):
        print(f"{red}You've let trough a person with forbidden possessions!\n-$20{white}")
    else:
        print(f"{green}Good decision comrade!\n+$10{white}")
        money = money + 10


def dontLetTrough():
    global money
    if (random_fname_chosen == first_person_name):
        print(f"{green}You've stopped a person with forbidden first name!\n+$30{white}")
        money = money + 30
    elif (random_lname_chosen == first_person_surname):
        print(f"{green}You've stopped a person with forbidden last name!\n+$30{white}")
        money = money + 30
    elif (random_age == first_person_age):
        print(f"{green}You've stopped a person with forbidden age!\n+$30{white}")
        money = money + 30
    elif (random_country_chosen == first_person_country):
        print(f"{green}You've stopped a person with forbidden origin country!\n+$30{white}")
        money = money + 30
    elif (first_person_possession == 'Gun' or first_person_possession == 'Knife'):
        print(f"{green}You've stopped a person with forbidden possessions!\n+$30{white}")
    else:
        print(f"{red}Could've let them trough!\n-$10{white}")
        money = money - 10


def borderCheck():
    border_input = input(f'Do you let this person trough the border? ({green}yes{white} or {red}no{white}): \n')
    newLine()
    if border_input.lower() == 'yes':
        letTrough()
    elif border_input.lower() == 'no':
        dontLetTrough()
    
def introduction():
    """
    Short introduction which takes the players name with a short description
    """
    newLine()
    typingPrint(f"Zdravstvuy {red}comrade{white}, welcome to the border. What's your name? \n")
    newLine()
    username = input("Type in your name and press return: \n")
    newLine()
    typingPrint(f'Well officer \033[1;32m{username} \033[1;37;40m, seems like you have got the short end of the stick today.\nThere are enemy spies all over the place. \n')
    typingPrint('The boss tells us who we can let in the motherland based on his information each day. \n')
    typingPrint('You will either gain money or lose it depending on how well you do.\n')
    



def finalScore():
    if money > 1:
        print(f'{green}You have ${money}!{white}')
    else:
        print(f'{red}You have {money} dollars!{white}')

def main():
    """
    Main function which calls others when required
    """
    introduction()
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
main()