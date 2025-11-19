
from abc import ABC, abstractmethod
from typing import final

class Game(ABC):
    
    @final
    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()
        
    def initialize(self):
        print("Getting all players ready for play.")
    
    @abstractmethod
    def start_play(self):
        pass
    
    @abstractmethod
    def end_play(self):
        pass
    