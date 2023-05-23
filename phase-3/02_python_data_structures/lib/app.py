# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

#! Lists
#TODO Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

#TODO Reading Information From Lists
#2. ✅ Return the first pet name
#3. ✅ Return all pet names beginning from the 3rd index [3:]
#4. ✅ Return all pet names before the 3rd index [:3]
#5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index [3:7]
#6. ✅ Find the index of a given element => .index() or .find()
#7. ✅ Read the original list in reverse order => [::-1] or destructively .reverse()
#8. ✅ Return the frequency of a given element => .count()

#TODO Updating Lists
#9. ✅ Change the first pet_name to all uppercase letters => .upper()
#10. ✅ Append a new name to the list => .append()
#11. ✅ Add a new name at a specific index => .insert()
#12. ✅ Add two lists together => +
#13. ✅ Remove the final element from the list => .pop()
#14. ✅ Remove element by specific index => .pop()
#15. ✅ Remove a specific element => .remove()
#16. ✅ Remove all pet names from the list => .clear()

#!Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable
    
    # Why Are Tuples Immutable?

        # What advantages does this provide for us? In what situations
        # would this serve us?
#TODO Accessing Elements
#17. ✅ Create an empty Tuple, one with one element and one with 10 pet ages => () 
#18. ✅ Print the first pet age => []

#TODO Testing Mutability (you can add a tuple to a tuple though)
#19. ✅ Attempt to remove an element with ".pop" (should error)
#20. ✅ Attempt to change the first element (should error) => []

#TODO Tuple Methods
#21. ✅ Return the frequency of a given element => .count()
#22. ✅ Return the index of a given element  => .index()

#! Range
#23. ✅ create a Range 
# Note:  Ranges are primarily used in loops

#! Sets (value cannot be modified but you can add/remove elements)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

#TODO Reading
#27. ✅ Print set elements with a loop
#27. ✅ Check if an element is in a set 
#27. ✅ Get random element => sample()
#27. ✅ Get first element => next(iter(set({1, 2, 3})))
#28. ✅ Print the pet attribute of "age" using ".get"
#28. ✅ Get a copy of a set => copy()
#28. ✅ isdisjointed, issubset, issuperset

#TODO Updating 
#29. ✅ Add an element to a set => add()
#30. ✅ Union, intersection, difference
#30. ✅ Update current set with elements from other set


#TODO Deleting
#31. ✅ Delete specific el using ".remove"  VS ".discard" => []
#32. ✅ Delete random element using ".pop"
#33. ✅ Delete the last item for Rose using "popitem()"
#33b ✅ Delete every key/value pair => clear()


#! Dictionaries (from 3.7+, dictionaries are ordered)
#TODO Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

#TODO Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['temperament'])

#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error
#28b. ✅ Get dict keys
#28c. ✅ Get dict values
#28d. ✅ Get dict pairs

#TODO Updating 
#29. ✅ Update Rose's age to 12 => []
#30. ✅ Update Spot's age to 26 => .update({...})

#TODO Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []
#32. ✅ Delete Spot's age using ".pop"
#33. ✅ Delete the last item for Rose using "popitem()"
#33b ✅ Delete every key/value pair => clear()


#! Loops 
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
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range
#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
#36. ✅ Loop through the "pet_info" list and print every dictionary
#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument
#38. ✅ Create a function that takes a list as a parameter
    # The function should define a variable ("counter") and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Once the loop has finished, return the final value of "counter"

#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'
    
#! Functional Programming corner
# map like VS map
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

# find like VS find
#41. ✅ Use list comprehension to find a pet named spot

# filter like VS filter
#42. ✅ Use list comprehension to find all of the pets under 3 years old

# reduce like VS reduce
#42. ✅ Use list comprehension to find all of the pets under 3 years old

#! Writing Generators
#43. ✅ Create a generator expression matching the filter above

