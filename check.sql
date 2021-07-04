USE pokemon;

-- SELECT * FROM pokemon;
-- SELECT * FROM trainer;
-- SELECT * FROM owned_by;

-- SELECT name AS heaviest FROM pokemon
-- WHERE weight = (SELECT MAX(weight) FROM pokemon);

-- SELECT t.name FROM pokemon p, owned_by o, trainer t WHERE p.id = o.pokemon_id AND t.id = o.trainer_id AND p.name = 'gengar'; 

-- SELECT max()
-- SELECT count.pokemon_id
-- FROM (
SELECT pokemon_id
, MAX(c)
FROM (
SELECT pokemon_id, COUNT(*) as c
FROM owned_by
GROUP BY pokemon_id
) as count