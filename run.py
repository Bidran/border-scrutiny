import time,os,sys

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


def main():
    typingPrint("Zdravstvuy comrade, welcome to the border. What's your name? \n")
    username = input("Type in your name and press return: \n")
    typingPrint(f'Well officer \033[1;32m {username} \033[1;37;40m, seems like you have got the short end of the stick today. \n')
    typingPrint('The boss tells us who we can let in the motherland based on his criteria each day. \n')
    typingPrint('Are you ready to begin? \n')
main()