#!/usr/bin/env python3

# from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.drop_table()
Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")
# spot.save()
Pet.create("fido", "dog", "pug", "feisty")
Pet.create("spot", "dog", "chihuahua", "feisty")
# Pet.get_all()
print(Pet.find_by_name('fido'))
print(Pet.find_by_id(3))
# fido = Pet.new_from_db()
print('done!')


# import ipdb; ipdb.set_trace()
