from genius import Genius
from giratron import Giratron
from player import Player
import ranking
import os
import inquirer


def introduction():
    print("\nWelcome to our Game!")
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
        
# Get player's information
def get_name():
    nickname = input("Insert your Nickname: ").title()
    return nickname


def get_edv():
    while(True):
        try:
            cpf = int(input("Insert your EDV: "))
            print("\n------------------------------------------------------------------\n")
            break
        except:
            print("You must enter only numbers")

    return cpf



# Do something using menu choice
def menu_choice(choice, player):
    match(choice):
        case 1:
            Genius.show_rules()
            Genius.show_items()
            genius = Genius()
            genius.start(player)

        case 2:
            Giratron.show_rules()
            Giratron.show_items()
            giratron = Giratron()
            giratron.start(player)

        case 3:
            ranking_df_genius = ranking.load_ranking("Sheet1")
            ranking_df_giratron = ranking.load_ranking("Sheet2")
            print("\n------------------------------------------------------------------\n")
            print("Genius Ranking:")
            print(ranking_df_genius)
            print("\n------------------------------------------------------------------\n")
            print("Giratron Ranking:")
            print(ranking_df_giratron)
            print("\n------------------------------------------------------------------\n")
            
        case 4:
            print("Well, if you want... Finishing...")
            exit()


def start():
    # Checking if the ranking excel exists
    if(not os.path.exists("ranking.xlsx")):
        ranking.create_ranking()

    introduction()
    player = Player(get_name(), get_edv())

    # Game process
    while(True):
        menu_choice(catch_choice(), player)

