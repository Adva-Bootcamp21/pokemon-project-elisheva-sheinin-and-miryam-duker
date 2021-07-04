USE pokemon;
CREATE TABLE pokemon(
  id INTEGER PRIMARY KEY NOT NULL,
  name VARCHAR(25),
  type VARCHAR (25),
  height INTEGER,
  weight INTEGER
);
CREATE TABLE trainer(
  id INTEGER PRIMARY KEY,
  name VARCHAR (25),
  town VARCHAR (25)
);
CREATE TABLE owned_by(
  pokemon_id INTEGER ,
  trainer_id INTEGER ,
  FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
  FOREIGN KEY (trainer_id) REFERENCES trainer(id),
  PRIMARY KEY (pokemon_id, trainer_id)
);
-- DROP TABLE owend_by;
-- DROP TABLE trainer;
-- DROP TABLE pokemon;
