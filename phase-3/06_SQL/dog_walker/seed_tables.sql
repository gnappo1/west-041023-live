
-- # Owners
INSERT INTO owners(name, address, email, phone) 
VALUES ('ix', '999 8th st Seattle Wa 90000', 'ix_is_cool@gmail.com', '9991231234');

INSERT INTO owners(name, address, email, phone) 
VALUES ('Adam', '000 dr sw San Francisco CA 90000', 'cyberpunk999@gmail.com', '0001239999');

-- # Pets
INSERT INTO dogs(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('Luke', '2', 'domestic longhair', 'bacon', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229064/zx6CPsp_d_utkmww.webp', 2);

INSERT INTO dogs(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('rose', '11', 'domestic longhair', 'house plants', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229038/EEE90-E50-25-F0-4-DF0-98-B2-0-E0-B6-F9-BAA89_menwgg.jpg', 1);


INSERT INTO dogs(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('leia', '2', 'domestic Shorthair', 'bacon', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229011/8136c615d670e214f80de4e7fcdf8607--cattle-dogs-mans_vgyqqa.jpg', 2);

INSERT INTO dogs(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('Chop', '5', 'shiba inu', 'cheese', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1629822267/cdbd77592e3ef91e8cc1cf67d936f94f_fkozjt.jpg', 1);

-- # Handlers

INSERT INTO handlers (name, email, phone) 
VALUES ('gannie', 'grannie52@gmail.com', '1239087654');
INSERT INTO handlers (name, email, phone) 
VALUES ('dorian', 'blue_boy@gmail.com', '8887776666');

-- -- # Appointments
INSERT INTO appointments (time, request, dog_id, handler_id) 
VALUES ('2022-07-31 00:00:00', 'drop-in', 1,1);

INSERT INTO appointments (time, request, dog_id, handler_id) 
VALUES ('2022-03-01 00:00:00', 'drop-in', 1,1);

INSERT INTO appointments (time, request, dog_id, handler_id) 
VALUES ('2022-06-01 00:00:00', 'drop-in', 1,2);

INSERT INTO appointments (time, request, dog_id, handler_id) 
VALUES ('2022-05-21 00:00:00', 'walk', 2,2);


