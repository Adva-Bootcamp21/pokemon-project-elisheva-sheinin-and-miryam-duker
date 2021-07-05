USE pokemon;

-- SELECT * FROM pokemon;
-- SELECT * FROM trainer;
-- SELECT * FROM owned_by;
-- SELECT * FROM types;
-- SELECT * FROM has_types;

-- SELECT p.name 
--                     FROM pokemon p, has_types h, types t 
--                     WHERE p.id = h.pokemon_id
--                     AND  h.type_id = t.id
--                     AND t.type_name = 'Grass'
-- SELECT name AS heaviest FROM pokemon
-- WHERE weight = (SELECT MAX(weight) FROM pokemon);

-- SELECT t.name FROM pokemon p, owned_by o, trainer t WHERE p.id = o.pokemon_id AND t.id = o.trainer_id AND p.name = 'gengar'; 

-- SELECT max()
-- SELECT count.pokemon_id
-- FROM (
-- SELECT pokemon_id
-- , MAX(c)
-- FROM (
-- SELECT pokemon_id, COUNT(*) as count
-- FROM owned_by
-- GROUP BY pokemon_id
-- ) as count
-- WHERE c = ALL( 
-- SELECT Max(c)


-- SELECT pokemon_id, count
-- FROM (
--     SELECT pokemon_id, COUNT(*) as count
-- FROM owned_by
-- GROUP BY pokemon_id) as A
-- WHERE count >= ALL(SELECT  COUNT(*)
--                 FROM owned_by
--                 GROUP BY pokemon_id)

-- SELECT * FROM pokemon WHERE name = "miryam";

-- INSERT INTO pokemon VALUES (160, 'miryam', 160, 40);
-- INSERT INTO types VALUES (160, '['a','b','c']');

-- CREATE TABLE try(
--     try_id INTEGER PRIMARY KEY ,
--     type VARCHAR(25) ARRAY[VARCHAR(25)]
-- );
