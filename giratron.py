from game import Game
from time import sleep
import os
import random
import inquirer
import pyttsx3

class Giratron(Game):

    items = ["1", "2", "3", "4", "5", "6", "Green", "Red", "White", "Yellow", "Purple", "Orange"]

    def __init__(self):
        super().__init__()


    @staticmethod
    def show_rules():
        print("In this game we have some numbers and colors. They'll be drawn and your function is to memorize and select them in the correct order!")

    
    @classmethod
    def show_items(cls):
        print("The items are:", cls.items)


    def start(self):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
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


    def draw_item(self):
        return random.choice(Giratron.items)
    

    def append_item(self, drawn_item):
        self.drawn_items.append(drawn_item)


    def ask_option(self):
        options = [
            inquirer.List('size',
            choices=["1", "2", "3", "4", "5", "6", "Green", "Red", "White", "Yellow", "Purple", "Orange"],
            )
        ]

        select = inquirer.prompt(options)
        return select['size']