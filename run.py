import time,os,sys,random
from random import choice

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)


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

possesion = [
    'Knife','Gun','Lighter','Cigarettes','Phone',
    'Chocolate','Crisps','Juice','Painting','Headphones','Laptop',
    'USB Stick', 'Broom', 'Rollerblades','Fidget Spinner','Lightbulb'
    ]

def makePerson():
    persons = [makeMan(), makeWoman()]
    chosen = random.choice(persons)
    print(chosen)
    

def makeMan():
    random_fname = random.choice(first_name_men)
    random_lname = random.choice(last_name_men)
    age = random.choice(range(10,100))
    random_country = random.choice(origin_country)
    random_possesion = random.sample(possesion, 3)
    return [random_fname,random_lname,age,random_country,random_possesion]
    
def makeWoman():
    random_fname = random.choice(first_name_women)
    random_lname = random.choice(last_name_women)
    age = random.choice(range(10,100))
    random_country = random.choice(origin_country)
    random_possesion = random.sample(possesion, 3)
    return [random_fname,random_lname,age,random_country,random_possesion]
    
makePerson()

def newLine():
    """
    Makes space for readability
    """
    print('\n')


def beginGame():
    """
    Takes players input if he wishes to proceed with the game.
    """
    user_input = input('Are you ready to begin? (yes/no): \n')
    if user_input.lower() == 'yes':
        print('user typed yes')
    elif user_input.lower() == 'no':
        typingPrint("Off to jail with you! \n")
        user_input_no = input('Did you change your mind? (yes/no): \n')
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

def introduction():
    """
    Short introduction which takes the players name with a short description
    """
    newLine()
    typingPrint("Zdravstvuy comrade, welcome to the border. What's your name? \n")
    newLine()
    username = input("Type in your name and press return: \n")
    newLine()
    typingPrint(f'Well officer \033[1;32m{username} \033[1;37;40m, seems like you have got the short end of the stick today. \n')
    typingPrint('The boss tells us who we can let in the motherland based on his criteria each day. \n')
    beginGame()


def main():
    introduction()
# main()