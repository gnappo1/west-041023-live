CREATE TABLE IF NOT EXISTS owners(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    address TEXT,
    phone INTEGER
);

CREATE TABLE IF NOT EXISTS dogs(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);

CREATE TABLE IF NOT EXISTS handlers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone INTEGER
);

CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY,
    time DATETIME,
    request TEXT,
    dog_id INTEGER,
    handler_id INTEGER,
    FOREIGN KEY (dog_id) REFERENCES dogs(id),
    FOREIGN KEY (handler_id) REFERENCES handlers(id)
);

-- Add columns to existing tables
-- ALTER TABLE dogs ADD COLUMN favorite_treats TEXT;
-- ALTER TABLE dogs ADD COLUMN last_fed DATETIME;
-- ALTER TABLE dogs ADD COLUMN image_url TEXT;

-- Drop tables
-- DROP TABLE owners;
-- DROP TABLE dogs;
