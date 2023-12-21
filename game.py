from abc import ABC, abstractmethod
import inquirer

class Game(ABC):
    def __init__(self):
        self.drawn_items = []

    @abstractmethod
    def show_rules():
        pass


    @abstractmethod
    def show_items():
        pass
    

    @abstractmethod
    def start(self):
        pass


    @abstractmethod
    def draw_item(self):
        pass


    @abstractmethod
    def ask_option(self):
        pass


    def append_item(self, drawn_item):
        self.drawn_items.append(drawn_item)


    def get_choice(self):
        options = [
            inquirer.List('size',
            message="Are you ready?",
            choices=["Yes", "No"]
            )
        ]

        select = inquirer.prompt(options)
        match(select['size']):
            case "Yes":
                return True
            case "No":
                return False