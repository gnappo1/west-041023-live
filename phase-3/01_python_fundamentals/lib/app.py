#!/usr/bin/env python3
import ipdb
# 📚 Review:
    # Python Environment Setup
	# Python Debugging Tools
	# Python Data Types 

# Conversation about Python
   # Which kind of language is it? (multi-paradigm, dynamically typed, interpreted CPython)
   # What is it used for?
   # Examples of websites relying on Python
   # Origin and Evolution
   # Current State of Python: BDFL Guido Von Rossum Abdicated, Steering Council (https://peps.python.org/pep-8104/)
   # Current version of Python 3.11.0

# Style Guide, Formatters, Indentation Rules
   # PEP8
   # Black
   # 4 Spaces

# Running your code
   # Run Code
   # Run Script -> chat about __name__ == '__main__'


# Debugging your code
   # ipdb -> # 🚨 To enable ipdb debugging, first import "ipdb" and then type ipdb.set_trace()
   # built-in debugger


# Data Types:
   # Boolean (True, False), Numeric (int, long, float, complex), String (unicode repr)
   # Sequence (list, tuple, range) Set (set, frozenset)
   # Mapping (dict), NoneType (None)


# Variables, Conventions and Scopes
   # leading underscore or letter
   # no leading numbers or special chars
   # case-sensitive
   # snakecase or all caps for constants
   # no special keyword for declaration, assignments required
   # deleting a variable
   # NameError exception
   # print("matteo is cool", "test 2 bello", sep="--", end="\n\n")
   # f-strings and format
pet_mood = "Rowdy!"
pet_name = "Rose"
print(pet_mood, pet_name, sep="-", end="\n\n")


# 3. Conditional Statements
#TODO 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."
if pet_mood == "Hungry!":
    print("Rose needs to be fed.")
elif pet_mood == "Rowdy!":
    print("Rose needs a walk.")
else:
    print("Rose is all good.")

# Note => Feel free to set your own values for "pet_mood" to view various outputs.

#TODO 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."
print("Rose needs to be fed.") if pet_mood == "Hungry!" else print( "Rose is all good.")
# nested ternaries
print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose is all good.") if pet_mood != "Rowdy!" else print( "Rose is all good.")

#TODO 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"
def say_hello():
    # global pet_name used to access global variables inside functions
    pet_name = 'matteo'
    return pet_name

print(say_hello())
print(pet_name)

#TODO 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"
def pet_greeting(name='Matteo'):
    return f'{name} says hello!'

pet_greeting('Matteo') # invoking with less args than the required ones raises TypeError
pet_greeting()

def test(first, second, *all, name, age, **kwargs):
    print(f'Required args: {first}, {second} ')
    print(f'Additional Extra args: {all} collected into a tuple')
    print(f'Key-value args: {name}, {age}')
    print(f'Additional Extra k-value args: {kwargs} collected into a tuple')
    
    ipdb.set_trace()

test("one", "two", True, 32, name="Matteo", age=31, job='educator')

#TODO 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."
def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!":
        print(f"{pet_name} needs to be fed.")
    elif pet_mood == "Rowdy!":
        print(f"{pet_name} needs a walk.")
    else:
        print(f"{pet_name} is all good.")
        
pet_status('Pongo', "Angry!")
# Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
# in Global Scope.

#TODO 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html
def pet_birthday(age):
    """_summary_

    Args:
        age (int): integer required param

    Returns:
        str: a congrats message
    """
    
    try:
        return f"Happy Birthday! Your pet is now {age + 1}"
    except Exception as e:
        # raise e
        return "Hey the argument has to be of type number"
    # if (type(age) == int):
    #     return f"Happy Birthday! Your pet is now {age + 1}"
    # else:
    #     return "Hey the argument has to be of type number"
    
print(pet_birthday({}))
print(pet_birthday.__doc__)

# Loops (for...in, while)
x = 0
while x < 5:
    print(x)
    x += 1
    
for _ in range(0, 5):
    print("Same thing printed 5 times")
    
# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()

# if __name__ == '__main__':
    # print(pet_mood)
