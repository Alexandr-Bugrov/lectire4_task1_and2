SELECT name, year_of_realise, FROM album
    WHERE year_of_realise >= 2018;

SELECT name, duration, FROM track
    ORDER BY duration
    LIMIT 1;

SELECT name FROM track
    WHERE duration >= 210;

SELECT name FROM collections
    WHERE year_of_realise BETWEEN 2018 AND 2020;

SELECT name FROM band
    WHERE name NOT IN (' ');

SELECT name FROM track
    WHERE name LIKE '%my%' OR name LIKE '%мой%';
    