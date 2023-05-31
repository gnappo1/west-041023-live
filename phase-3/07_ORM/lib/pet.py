# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet:
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, id=None):
        self.name, self.species, self.breed, self.temperament, self.id = name, species, breed, temperament, id

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS pets(
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT
            );
        """)
        CONN.commit()
    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS pets;
        """)
        CONN.commit()
    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        # self is only instantiated so it has no id
        CURSOR.execute("""
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?);       
        """, [self.name, self.species, self.breed, self.temperament])
        CONN.commit()
        # the obj represented by self made it into the db
        # now we need to assign them the correct id the table allocated
        # now we need to figure out how to retrieve the id from the last db row
        self.id = CURSOR.lastrowid
        
    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament):
        # Initialize a new obj with the info provided
        new_pet = cls(name, species, breed, temperament)
        # save the obj to make sure it's in the db
        new_pet.save()
        return new_pet

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_from_db(cls):
        CURSOR.execute("""
            SELECT * FROM pets
            ORDER BY id DESC
            LIMIT 1;
        """)
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0])

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        CURSOR.execute("""
            SELECT * FROM pets; 
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("""
            SELECT * FROM pets
            WHERE name is ?;
        """, (name, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None

        # If No "pet" Found, return "None"

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("""
            SELECT * FROM pets
            WHERE id is ?;
        """, (id, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None

        # If No "pet" Found, return "None"

    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by(cls, name, species, breed, temperament):
        cls.find_by_name(name) or cls.create(name, species, breed, temperament)
        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
    def update(self):
        CURSOR.execute("""
            UPDATE pets
            SET name=?, species=?, breed=?, temperament=?
            WHERE id = ?
        """, (self.name, self.species, self.breed, self.temperament, self.id))
        CONN.commit()
        return type(self).find_by_id(self.id)