from genius import Genius
from giratron import Giratron
import inquirer


def introduction():
    print("Welcome to our Game!")
    print("Here we have Genius and Giratron.")
    print("Genius: PC will say some numbers and you'll memorize the sequence and write it.")
    print("Giratron: PC will say some numbers and coloros and you'll memorize the sequence and write it..")
    print("\n------------------------------------------------------------------\n")
    
    
# Code block to catch menu choice
def catch_choice():
    questions = [
        inquirer.List('size',
        message="Do you want to...",
        choices=['Play Genius', 'Play Giratron', 'Show ranking', 'Exit'],
        )
    ]

    select = inquirer.prompt(questions)
    match(select['size']):
        case "Play Genius":
            return 1
        case "Play Giratron":
            return 2
        case "Show ranking":
            return 3
        case "Exit":
            return 4
        

# Do something using menu choice
def menu_choice(choice):
    match(choice):
        case 1:
            Genius.show_rules()
            Genius.show_items()
            genius = Genius()
            genius.start()
        case 2:
            Giratron.show_rules()
            Giratron.show_items()
            giratron = Giratron()
            giratron.start()
        case 3:
            pass
        case 4:
            print("Well, if you want... Finishing...")
            exit()


def start():
    introduction()
    # Game process
    while(True):
        menu_choice(catch_choice())


start()
