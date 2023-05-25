# import ipdb

# 7. ✅. Create a subclass of Pet called Cat
    
from pet import Pet

class Cat(Pet):
    def __init__(self, outdoor, **kwargs):
        # run the parent's init
        super().__init__(**kwargs)
        # but also, set an extra attribute pls
        self._outdoor = outdoor

    def meow(self):
        return "Meow!"
    
    def print_pet_details(self):
        super().print_pet_details()
        print(f'Outdoor:{self._outdoor}')
    
spidey = Cat(True, name="Fido", age=2, breed="pug", temperament="docile", owner="Matteo")
