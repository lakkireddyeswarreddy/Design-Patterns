from abc import ABC, abstractmethod

class API(ABC):
    
    @abstractmethod
    def get_user_details(self):
        pass