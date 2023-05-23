# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

#! Lists
#TODO Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

#TODO Reading Information From Lists
#2. ✅ Return the last pet name
print(pet_names[-1])
#3. ✅ Return all pet names beginning from the 3rd index [3:]
print(pet_names[3:])
#4. ✅ Return all pet names before the 3rd index [:3]
print(pet_names[:3])
#5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index [3:7]
print(pet_names[3:8])
print(pet_names[3:8:2])
#6. ✅ Find the index of a given element => .index()
print(pet_names.index("rose"))
#7. ✅ Read the original list in reverse order => [::-1] or destructively .reverse()
print(pet_names[::-1]) #* non-destructive
print(pet_names.reverse()) #! destructive
print(pet_names)
#8. ✅ Return the frequency of a given element => .count()
print(pet_names.count('Rose'))

#TODO Updating Lists
#9. ✅ Change the first pet_name to all uppercase letters => .upper() NON-DESTRUCTIVE
pet_names[0] = pet_names[0].upper()
#10. ✅ Append a new name to the list => .append() DESTRUCTIVE
pet_names.append("Matteo")
#11. ✅ Add a new name at a specific index => .insert() DESTRUCTIVE
pet_names.insert(22, "Matteo")
#12. ✅ Add two lists together => + NON-DESTRUCTIVE
print(pet_names + ["Matteo"])
#13. ✅ Remove the final element from the list => .pop() DESTRUCTIVE
print(pet_names.pop())
#14. ✅ Remove element by specific index => .pop() DESTRUCTIVE
print(pet_names.pop(0))
print(pet_names.pop(11))
print(pet_names)
#15. ✅ Remove a specific element => .remove() DESTRUCTIVE
print(pet_names.remove("Rose"))
#16. ✅ Remove all pet names from the list => .clear() DESTRUCTIVE
# print(pet_names.clear())
print(pet_names)

#!Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable
    
    # Why Are Tuples Immutable?

        # What advantages does this provide for us? In what situations
        # would this serve us?
#TODO Accessing Elements
#17. ✅ Create an empty Tuple, one with one element and one with 10 pet ages => ()
empty_tuple = ()
one_el_tuple = (2, )
tuple_coll = (3, 4, 5, 6, 3)

#18. ✅ Print the first pet age => []
empty_tuple #=> empty_tuple[0] Returns error IndexError: tuple index out of range
one_el_tuple[0]
tuple_coll[0]

#TODO Testing Mutability (you can add a tuple to a tuple though)
#19. ✅ Attempt to remove an element with ".pop" (should error)
#20. ✅ Attempt to change the first element (should error) => []

#TODO Tuple Methods
#21. ✅ Return the frequency of a given element => .count()
print(tuple_coll.count(33))
#22. ✅ Return the index of a given element  => .index() you get the index of the FIRST match
print(tuple_coll.index(3))

#! Range
#23. ✅ create a Range 
# Note:  Ranges are primarily used in loops
r = range(10)
next(r)

#! Sets (value cannot be modified but you can add/remove elements)
#24. ✅ Create a set of 3 pet foods and an empty set
s = set({})
pet_fav_food = {'house plants', 'fish', 'bacon'}

#TODO Reading
# #27. ✅ Print set elements with a loop
for el in pet_fav_food:
    print(el)
#27. ✅ Check if an element is in a set
print('fish' in pet_fav_food)
#27. ✅ Get random element => sample() imported from random and extra step for sets
print(pet_fav_food.sample())
#27. ✅ Get first element => next(iter(set({1, 2, 3})))
i = iter(set({1, 2, 3}))

#28. ✅ Get a copy of a set => copy()
s2 = pet_fav_food.copy()
#28. ✅ isdisjoint, issubset, issuperset
s.isdisjoint(s2)

#TODO Updating 
# #29. ✅ Add an element to a set => add()
pet_fav_food.add("gnocchi")
# #30. ✅ Union, intersection, difference if using destructive versions because they would be non-destructive otherwise
pet_fav_food.union(s2)
# #30. ✅ Update current set with elements from other set DESTRUCTIVE
pet_fav_food.update(s2)


#TODO Deleting
#31. ✅ Delete specific el using ".remove"  VS ".discard" => []
    # the only difference pertains error handling, where discard is more flexible
pet_fav_food.discard("gnocchi")
# #32. ✅ Delete random element using ".pop"
pet_fav_food.pop()
# #33b ✅ Delete every => clear() DESTRUCTIVE
pet_fav_food.clear()


#! Dictionaries (from 3.7+, dictionaries are ordered)
#TODO Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

#TODO Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
print(pet_info_rose['temperament'])

#28. ✅ Print the pet attribute of "age" using ".get"
    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error
print(pet_info_rose.get('temperament', "key is not in dict"))

#28b. ✅ Get dict keys
print(pet_info_rose.keys())
#28c. ✅ Get dict values
print(pet_info_rose.values())
#28d. ✅ Get dict pairs
print(pet_info_rose.items())

#TODO Updating 
#29. ✅ Update Rose's age to 12 => []

pet_info_rose['age'] = 39
print(pet_info_rose)
#30. ✅ Update Spot's age to 26 => .update({...})
pet_info_rose.update({'age': 26, 'test': 30})

#TODO Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []
del pet_info_rose['name']
#32. ✅ Delete Spot's age using ".pop"
        #! remove k/v pair but return only the value
pet_info_rose.pop('name')
#33. ✅ Delete the last item for Rose using "popitem()"
        #! remove k/v pair and return both as tuple
pet_info_rose.popitem()
#33b ✅ Delete every key/value pair => clear()
pet_info_rose.clear()


# #! Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    },{
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range
my_range = range(10)

for num in my_range:
    print(num)

#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
my_range = range(50, 60, 2)

for num in my_range:
    print(num)

#36. ✅ Loop through the "pet_info" list and print every dictionary 

for pet in pet_info:
    print(pet)

#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument

def output_pet_names(list):
    for pet in list:
        print(pet)  

output_pet_names(pet_info)

#38. ✅ Create a function that takes a list as a parameter
    # The function should define a variable ("counter") and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Once the loop has finished, return the final value of "counter"

def return_pet_count(list):

    counter = 0

    while(counter < len(list)):
        counter += 1

    return counter

print(return_pet_count(pet_info))

#39. ✅ Create a function that updates the age of a given pet
        # DONE - The function should take a list of "dictionaries", "name" and "age" as parameters 
        # DONE - Create an index variable and set it to 0
        # Create a while loop 
            # DONE - The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # DONE - Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

def update_pet_age(list, name, age):

    # Set "index" Counter for While Loop
    index = 0

    # While the "name" attribute of the index-specified Dictionary IS NOT equal to
    # the "name" passed in AND the "index" is LESS than the length of "list" - 1
    # (to account for indices)....
    while(list[index]['name'] != name and index < len(list) - 1):

        # ...continue to increment "index" up by 1
        index += 1

    # If the "name" attribute of the index-specified Dictionary IS equal to
    # the "name" passed...
    if (list[index]['name'] == name): 
        
        # ...update the "age" attribute of the index-specified Dictionary to be
        # the "age" passed into "update_pet_age"...
        list[index]['age'] = age

        # ...before finally returning the new "list" with updated Dictionary
        return list    

    # Otherwise, return "Pet Not Found!"
    else: 
        return 'Pet Not Found!'

# When a Pet IS NOT Found
print(update_pet_age(pet_info, 'XYZ', 12))

# When a Pet IS Found
print(update_pet_age(pet_info, 'Rose', 12))

# ADDITIONAL CONTENT

# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
print(pet_info)
new_pet_list = [pet.get('name').upper() for pet in pet_info]
print(new_pet_list)
print(pet_info)

# find like
#41. ✅ Use list comprehension to find a pet named spot
# spot = [RETURNED PET / LOOP / CONDITIONAL]
spot = [pet for pet in pet_info if pet.get("name") == 'Spot' ]
print(spot[0])

# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old
# young_pets = [RETURNED PET / LOOP / CONDITIONAL]
young_pets = [pet for pet in pet_info if pet.get("age") < 2]
print(len(young_pets))

#43. ✅ Create a generator expression matching the filter above

# Main Benefit => Less Memory Intensive

young_pets_gen = (pet for pet in pet_info if pet.get("age") < 26)

# Accessing Generator Object Values

# 1. Using next()
print(next(young_pets_gen))
print(next(young_pets_gen))
print(next(young_pets_gen))

# 2. Using a for loop
for pet in young_pets_gen:
    print(pet)


#! Compare Generators and Expressions
import sys
import timeit
starter_list = list(range(100000))

#! MEMORY
print("List Comprehension Memory Size", sys.getsizeof([el for el in starter_list if el%2==0]))
# 444376
print("Generator Expression Memory Size",sys.getsizeof((el for el in starter_list if el%2==0)))
#208

#! RUNTIME
print("Comprehension Run 1 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1))
#=> 0.005183833185583353
print("Comprehension Run 1000 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1000))
# => 2.4483373747207224
print("Generator Run 1 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1))
# => 9.041279554367065e-06
print("Generator Run 1000 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1000))
# => 0.00024854158982634544