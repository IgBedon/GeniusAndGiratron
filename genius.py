from game import Game
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


    @staticmethod
    def show_rules():
        print("In this game we have some numbers. They'll be drawn and your function is to memorize and select them in the correct order!")

    
    @classmethod
    def show_items(cls):
        print("The items are:", cls.items, "\n")


    def start(self, player):
        # Defining variables and configuring engine settings
        engine = pyttsx3.init()
        engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        voice_rate = 0
        lose = False
        stage = 1

        # Drawing the first four items
        for _ in range(4):
            self.append_item(self.draw_item())
        
        # Checking if player is ready
        choice = self.get_choice()
        if(choice):

            print("Starting in")

            while(not lose):
                round = 0
                for sec in range(3):
                    print(f"{sec+1}...")
                    sleep(1)
                print()

                # Increasing speed and drawing/saying one more item
                engine.setProperty("rate", 150 + voice_rate)
                engine.say(self.drawn_items)
                engine.runAndWait()

                # Checking the answer
                while(True):
                    selected_option = self.ask_option()

                    if(self.drawn_items[round] != selected_option):
                        lose = True
                        break
                    else:
                        round += 1
                
                    if(len(self.drawn_items) == round):
                        break

                # Going to the next level
                if(not lose):
                    os.system('cls')
                    print("====================================================\n")
                    print("Yeah! You're right!")
                    self.append_item(self.draw_item())
                    voice_rate += 10
                    stage += 1
            
            # Case the player loses
            os.system('cls')
            print("====================================================\n")
            print("You are wrong! The correct order was: ", self.drawn_items)
            print(f"You lost on {stage}° stage!")
            print("Finishing")
            for sec in range(3):
                print(f"{sec+1}...")
                sleep(1)
            print()

            player.set_stage(stage)

            # Ranking Part (Load, change and update)
            ranking_df = ranking.load_ranking("Sheet1")
            new_ranking_df = ranking.set_ranking(ranking_df, player)
            ranking.update_ranking(new_ranking_df, "Sheet1", "Sheet2")

        else:
            print("Ok, we can try again later!\n\n")

    # Some support methods
            
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
