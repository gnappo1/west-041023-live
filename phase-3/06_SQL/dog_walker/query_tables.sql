-- READ DATA

SELECT
    dogs.name,
    handlers.name,
    appointments.request,
    appointments.time
FROM appointments
JOIN dogs
    ON appointments.pet_id = dogs.id
JOIN handlers
    ON appointments.handler_id = handlers.id

-- READ DATA BY CONDITION

SELECT DISTINCT
    dogs.name,
    handlers.name
FROM appointments
JOIN dogs
    ON appointments.pet_id = dogs.id
JOIN handlers
    ON appointments.handler_id = handlers.id
WHERE dogs.name = 'Luke'
