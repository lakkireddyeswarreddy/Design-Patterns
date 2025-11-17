
class Pizza:
    
    def __init__(self):
        self._size = None
        self._crust = None
        self._topings = list()
        self._cheese_type = None
        
    def __repr__(self):
        return f"Pizza with {self._size} size, {self._crust} crust, {self._topings} topings, {self._cheese_type} cheese type"
    
class PizzaBuilder:
    
    def __init__(self):
        self._pizza = Pizza()
        
    def set_size(self, size):
        self._pizza._size = size
        return self
    
    def set_crust(self, crust):
        self._pizza._crust = crust
        return self
    
    def set_topings(self, topings :list):
        self._pizza._topings = topings[:]
        return self
    
    def set_cheese_type(self, cheese_type):
        self._pizza._cheese_type = cheese_type
        return self
    
    def build(self):
        return self._pizza

if __name__ == "__main__":
    pizza_obj = PizzaBuilder().set_size("Medium").set_crust("Thin").set_topings(["Chillies", "Onion", "Tomato"]).set_cheese_type("Mild").build()
    print(pizza_obj)
        