#!/usr/bin/env python3
# Class Attributes and Methods 

# import ipdb

ALLOWED_LIST = ['name', 'age', 'temperament', 'breed', 'owner']

class Pet:
# ✅ Define a class attribute (total_pets) and set it to 0

    # __slots__= '_name', '_age', '_temperament', '_breed', '_owner'
    all = []
    # What happens with our instances when we add a class attribute?
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, f'_{k}', v) if k in ALLOWED_LIST else None
            # self._name, self.age, self.breed, self.temperament, self.owner = name, age, breed, temperament, owner
        type(self).save(self)
    # Using Property to control the behavior of attributes
    @classmethod #=> classmethod()
    def save(cls, new_obj):
        cls.all.append(new_obj)
    
    @classmethod
    def find_by(cls, attr, val): # find_by('name', 'Fido')
        # return [pet for pet in cls.all if pet.__dict__[f'_{attr}'] == val]
        final_list = [pet for pet in cls.all if getattr(pet, attr) == val]
        return final_list[0] if final_list else "Sorry the pet doesn't seem to be in our records"
    
    @classmethod
    def find_by2(cls, attr, val): # find_by('name', 'Fido')
        for pet in cls.all:
            if getattr(pet, attr) == val:
                return pet
        return "Sorry the pet doesn't seem to be in our records"
        
    @classmethod
    def find_by3(cls, attr, val): # find_by('name', 'Fido')
        return next(
            (pet for pet in cls.all if getattr(pet, attr) == val),
            "Sorry the pet doesn't seem to be in our records",
        )
        
    @classmethod
    def filter_by(cls, attr, val): # find_by('name', 'Fido')
        # return [pet for pet in cls.all if pet.__dict__[f'_{attr}'] == val]
        return [pet for pet in cls.all if getattr(pet, attr) == val]

    @staticmethod
    def static(pay, hours, sick_days):
        print(pay, hours, sick_days)
        
    @property
    def name(self):
        print("Inside the name property getter")
        return self._name
    
    @name.setter
    def name(self, new_name):
        print("Inside the name property setter")
        if type(new_name) is str and len(new_name) > 2:
            self._name = new_name
        else:
            raise TypeError("Value must be a string with more than 2 chars")
        
    # name = property(get_name, set_name)
    
    def get_breed(self):
        print("Inside the breed property getter")
        return self._breed
    
    def set_breed(self, new_breed):
        print("Inside the breed property setter")
        if type(new_breed) is str and len(new_breed) > 2:
            self._breed = new_breed
        else:
            raise TypeError("Value must be a string with more than 2 chars")
        
    breed = property(get_breed, set_breed)
    
    def get_age(self):
        print("Inside the age property getter")
        return self._age
    
    def set_age(self, new_age):
        print("Inside the age property setter")
        if type(new_age) is int and new_age > 0:
            self._age = new_age
        else:
            raise TypeError("Value must be an int greater than 0")
        
    age = property(get_age, set_age)
    
    def get_owner(self):
        print("Inside the owner property getter")
        raise AttributeError('Privacy concern, you cannot see me!')
    
    def set_owner(self, new_owner):
        print("Inside the owner property setter")
        if type(new_owner) is str and len(new_owner) > 2:
            self._owner = new_owner
        else:
            raise TypeError("Value must be an string greater than 2")
        
    owner = property(get_owner, set_owner)
    
    def get_temperament(self):
        print("Inside the temperament property getter")
        raise AttributeError('Privacy concern, you cannot see me!')
    
    def set_temperament(self, new_temperament):
        print("Inside the temperament property setter")
        if type(new_temperament) is str and len(new_temperament) > 2:
            self._temperament = new_temperament
        else:
            raise TypeError("Value must be an string greater than 2")
        
    temperament = property(get_temperament, set_temperament)

    # def __repr__(self) -> str:
    #     return f'Hello, I am {self.name} and I am {self.age} y.o.'
        
    # Providing a fallback for property lookup, is always run after __getattribute__ if both are present!
    def __getattr__(self, name):
        print('Inside __getattr__')
        return f'No attribute called {name}'
    
    # Invoked before every getter property lookup! Useful to set rules and limitations to several attributes
    def __getattribute__(self, name):
        print('Inside __getattribute__')
        return object.__getattribute__(self, name)

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            owner:{self.owner}
        ''')

fido = Pet(name="Fido", xyz="xyz", age=2, breed="pug", temperament="docile", owner="Matteo")
milo = Pet(name="Milo", xyz="xyz", age=2, breed="pug", temperament="docile", owner="Matteo")
print('done')
# ✅. Create a class method increase_pets that will increment total_pets

    # Instance Method

    # Class Method