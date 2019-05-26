CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  origin VARCHAR NOT NULL,
  destination VARCHAR NOT NULL,
  duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 445);

SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500 AND destination = 'Paris';
SELECT * FROM flights WHERE duration > 500 OR destination = 'Paris';
SELECT AVG(duration) FROM flights;
SELECT AVG(duration) FROM flights WHERE origin = 'New York';
SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM flights WHERE origin = 'New York';
SELECT MIN(duration) FROM flights;
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%';
