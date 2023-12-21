from game import Game
from player import Player
import ranking
from time import sleep
import os
import random
import inquirer
import pyttsx3

class Genius(Game):

    items = ["Green", "Red", "Blue", "Yellow"]

    def __init__(self):
        super().__init__()
        self.player = Player(self.get_name(), self.get_edv())


    @staticmethod
    def show_rules():
        print("In this game we have some numbers. They'll be drawn and your function is to memorize and select them in the correct order!")

    
    @classmethod
    def show_items(cls):
        print("The items are:", cls.items, "\n")


    def start(self, ranking_df):
        engine = pyttsx3.init()
        engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        voice_rate = 0
        lose = False
        stage = 1

        for _ in range(4):
            self.append_item(self.draw_item())
        
        choice = self.get_choice()
        if(choice):

            print("Starting in")

            while(not lose):
                round = 0
                for sec in range(3):
                    print(f"{sec+1}...")
                    sleep(1)
                print()

                engine.setProperty("rate", 150 + voice_rate)
                engine.say(self.drawn_items)
                engine.runAndWait()


                while(True):
                    selected_option = self.ask_option()

                    if(self.drawn_items[round] != selected_option):
                        lose = True
                        break
                    else:
                        round += 1
                
                    if(len(self.drawn_items) == round):
                        break

                if(not lose):
                    os.system('cls')
                    print("====================================================\n")
                    print("Yeah! You're right!")
                    self.append_item(self.draw_item())
                    voice_rate += 10
                    stage += 1
            
            os.system('cls')
            print("====================================================\n")
            print("You are wrong! The correct order was: ", self.drawn_items)
            print(f"You lost on {stage}° stage!")
            print("Finishing")
            for sec in range(3):
                print(f"{sec+1}...")
                sleep(1)
            print()


            ranking.set_ranking(ranking_df, self.player)


        else:
            print("Ok, we can try again later!\n\n")


    def get_name(self):
        nickname = input("Insert your Nickname: ").title()
        return nickname
    

    def get_edv(self):
        while(True):
            try:
                cpf = int(input("Insert your EDV: "))
                break
            except:
                print("You must enter only numbers")

        return cpf


    def draw_item(self):
        return random.choice(Genius.items)


    def ask_option(self):
        options = [
            inquirer.List('size',
            choices=["Green", "Red", "Blue", "Yellow"],
            )
        ]

        select = inquirer.prompt(options)
        return select['size']
