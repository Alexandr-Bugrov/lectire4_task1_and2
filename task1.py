import sqlalchemy as sql

engine = sql.create_engine('postgresql://postgres:19851234@localhost:5432/lecture4')
connection = engine.connect()


def band():
    connection.execute("""INSERT INTO band(name)
        VALUES('Ария');
    INSERT INTO band(name)
        VALUES('Rammstein');
    INSERT INTO band(name)
        VALUES('AC/DC');
    INSERT INTO band(name)
        VALUES('Гражданская оборона');
    INSERT INTO band(name)
        VALUES('Mozart');
    INSERT INTO band(name)
        VALUES('Manowar');
    INSERT INTO band(name)
        VALUES('Майкл Джексон');
    INSERT INTO band(name)
        VALUES('Любэ');
    """)


def genre():
    connection.execute("""INSERT INTO genre(name)
        VALUES('Pop');
    INSERT INTO genre(name)
        VALUES('Industrial metal');
    INSERT INTO genre(name)
        VALUES('Classical');
    INSERT INTO genre(name)
        VALUES('Heavy metal');
    INSERT INTO genre(name)
        VALUES('Russian rock');
    """)


def album():
    connection.execute("""INSERT INTO album(name, year_of_realise)
        VALUES('Number Ones', 2003);
    INSERT INTO album(name, year_of_realise)
        VALUES('Super album', 2018);
    INSERT INTO album(name, year_of_realise)
        VALUES('Плохой альбом', 2022);
    INSERT INTO album(name, year_of_realise)
        VALUES('Замечательный альбом', 2021);
    INSERT INTO album(name, year_of_realise)
        VALUES('Rosenrot', 2015);
    INSERT INTO album(name, year_of_realise)
        VALUES('Здорово и вечно', 1989);
    INSERT INTO album(name, year_of_realise)
        VALUES('Battle Hymns', 1980);
    INSERT INTO album(name, year_of_realise)
        VALUES('Fly On The Wall', 1985);
    """)


def track():
    connection.execute("""INSERT INTO track(album_id, name, duration)
        VALUES(1 'You Rock My World', 265);
    INSERT INTO track(album_id, name, duration)
        VALUES(1 'Triller', 311);
    INSERT INTO track(album_id, name, duration)
        VALUES(2, 'Длинный трек', 500);
    INSERT INTO track(album_id, name, duration)
        VALUES(2, 'Короткий трек', 100);
    INSERT INTO track(album_id, name, duration)
        VALUES(3, 'Плохой трек', 150);
    INSERT INTO track(album_id, name, duration)
        VALUES(3, 'Ужасный трек', 199);
    INSERT INTO track(album_id, name, duration)
        VALUES(4, 'Сносный трек', 325);
    INSERT INTO track(album_id, name, duration)
        VALUES(4, 'Нормально', 189);
    INSERT INTO track(album_id, name, duration)
        VALUES(5, 'Rosenrot', 345);
    INSERT INTO track(album_id, name, duration)
        VALUES(5, 'Benzin', 445);
    INSERT INTO track(album_id, name, duration)
        VALUES(6, 'Моя оборона', 240);
    INSERT INTO track(album_id, name, duration)
        VALUES(6, 'Здорово и вечно', 445);
    INSERT INTO track(album_id, name, duration)
        VALUES(7, 'Manowar', 450);
    INSERT INTO track(album_id, name, duration)
        VALUES(7, 'Battle Hymn', 635);
    INSERT INTO track(album_id, name, duration)
        VALUES(8, 'Danger', 636);
    """)


def collection():
    connection.execute("""INSERT INTO collection(name, year_of_realise)
        VALUES('Зарубежный рок', 2014);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Классическая музыка', 2013);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Pop music', 2020);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Отечественный исполнитель', 2015);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Лучшее за 20 век', 2000);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Худшее за 20 век', 2018);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Сборик 20.22 год', 2022);
    INSERT INTO collection(name, year_of_realise)
        VALUES('Русский рок', 2022);
    """)


def tracks_in_collection():
    connection.execute("""INSERT INTO tracks_in_collection(track, collection)
        VALUES(15, 1);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(14, 1);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(13, 1);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(3, 2);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(4, 2);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(7, 3);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(6, 3);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(5, 6);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(5, 7);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(9, 4);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(10, 4);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(5, 5);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(6, 6);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(7, 7);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(6, 7);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(12, 8);
    INSERT INTO tracks_in_collection(track, collection)
        VALUES(13, 8);
    """)


def band_album():
    connection.execute("""INSERT INTO band_album(band, album)
        VALUES(1, 3);
    INSERT INTO band_album(band, album)
        VALUES(2, 5);
    INSERT INTO band_album(band, album)
        VALUES(3, 8);
    INSERT INTO band_album(band, album)
        VALUES(4, 6);
    INSERT INTO band_album(band, album)
        VALUES(5, 2);
    INSERT INTO band_album(band, album)
        VALUES(6, 7);
    INSERT INTO band_album(band, album)
        VALUES(7, 1);
    INSERT INTO band_album(band, album)
        VALUES(8, 4);""")


def band_genre():
    connection.execute("""INSERT INTO band_genre(band, genre)
        VALUES(1, 5);
    INSERT INTO band_genre(band, genre)
        VALUES(2, 2);
    INSERT INTO band_genre(band, genre)
        VALUES(3, 4);
    INSERT INTO band_genre(band, genre)
        VALUES(4, 5);
    INSERT INTO band_genre(band, genre)
        VALUES(5, 3);
    INSERT INTO band_genre(band, genre)
        VALUES(6, 4);
    INSERT INTO band_genre(band, genre)
        VALUES(7, 1);
    INSERT INTO band_genre(band, genre)
        VALUES(8, 1);
    INSERT INTO band_genre(band, genre)
        VALUES(8, 5);
""")


if __name__ == '__main__':
    band()
    album()
    track()
    genre()
    collection()
    tracks_in_collection()
    band_album()
    band_genre()