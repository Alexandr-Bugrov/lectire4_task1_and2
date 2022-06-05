SELECT name, year_of_realise, FROM album
    WHERE year_of_realise >= 2018;

SELECT track_name, duration, FROM track
    ORDER BY duration
    LIMIT 1;

SELECT track_name FROM track
    WHERE duration >= 210;

SELECT collections_name FROM collections
    WHERE year_of_realise BETWEEN 2018 AND 2020;

SELECT band_name FROM band
    WHERE band_name NOT LIKE ('% %');

SELECT track_name FROM track
    WHERE track_name LIKE '%my%' OR name LIKE '%мой%';
    