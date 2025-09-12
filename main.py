import sqlite3

# this file creates the normalized tables in sQL using python


conn=sqlite3.connect("netflix.db")
cursor=conn.cursor()


cursor.execute("""
create table if not exists Show(
    show_id INTEGER primary key,
    title TEXT,
    type TEXT,
    release_year INTEGER,
    description TEXT,
    popularity REAL,
    vote_count INTEGER,
    vote_average REAL,
    budget REAL,
    revenue REAL,
    date_added TEXT
);          
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Actor (
    actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ShowActor (
    show_id INTEGER,
    actor_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES Show(show_id),
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);
""")
cursor.execute("""
create table if not exists Language(
    lang_id INTEGER primary key,
    name text);
               """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS ShowLang (
    show_id INTEGER,
    lang_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES Show(show_id),
    FOREIGN KEY (lang_id) REFERENCES Language(lang_id)
);
""")
cursor.execute("""
create table if not exists Genre(
    genre_id INTEGER primary key,
    type text);
               """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS ShowGenre (
    show_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES Show(show_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);
""")

cursor.execute("""
create table if not exists Director(
    director_id INTEGER primary key,
    dir_name text);
               """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS ShowDirector (
    show_id INTEGER,
    director_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES Show(show_id),
    FOREIGN KEY (director_id) REFERENCES Genre(director_id)
);
""")
cursor.execute("""
create table if not exists Country(
    country_id INTEGER primary key,
    country_name text);
               """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS ShowCountry (
    show_id INTEGER,
    country_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES Show(show_id),
    FOREIGN KEY (country_id) REFERENCES Country(country_id),
    PRIMARY KEY (show_id, country_id)
);
""")

conn.commit()
conn.close()