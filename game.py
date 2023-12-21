from abc import ABC, abstractmethod

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
    def append_item(self):
        pass


    @abstractmethod
    def ask_option(self):
        pass