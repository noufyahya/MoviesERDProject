import pandas as pd
import sqlite3

#This is the final file that moves the data from the flat csv to sql

# Load Netflix dataset
df = pd.read_csv("netflix_movies_detailed_up_to_2025.csv")

conn=sqlite3.connect("netflix.db")
cursor=conn.cursor()

#Shows insert
# # Insert into Show table
# for _, row in df.iterrows():
#     cursor.execute("""
#     INSERT OR IGNORE INTO Show
#     (show_id, title, type, release_year, description, popularity, 
#      vote_count, vote_average, budget, revenue, date_added)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
#     """, (
#         int(row['show_id']) if not pd.isna(row['show_id']) else None,
#         row['title'],
#         row['type'],
#         int(row['release_year']) if not pd.isna(row['release_year']) else None,
#         row['description'],
#         float(row['popularity']) if not pd.isna(row['popularity']) else None,
#         int(row['vote_count']) if not pd.isna(row['vote_count']) else None,
#         float(row['vote_average']) if not pd.isna(row['vote_average']) else None,
#         float(row['budget']) if not pd.isna(row['budget']) else None,
#         float(row['revenue']) if not pd.isna(row['revenue']) else None,
#         row['date_added']
#     ))

# Check if shows were inserted correctly
cursor.execute("SELECT COUNT(*) FROM Show")
show_count = cursor.fetchone()[0]
print(f"Total shows in database: {show_count}")  # Should match your CSV row count

# Sample check
cursor.execute("SELECT * FROM Show LIMIT 3")
sample_shows = cursor.fetchall()
print("Sample shows:", sample_shows)

#all countries unique
# all_countries = set()
# for _, row in df.iterrows():
#     if pd.notna(row['country']):
#         countries = [c.strip() for c in str(row['country']).split(",")]
#         all_countries.update(countries)

# print(f"Found {len(all_countries)} unique countries")  # Should be ~100-200

# for country in sorted(all_countries):
#     cursor.execute("INSERT OR IGNORE INTO Country (country_name) VALUES (?)", (country,))

# cursor.execute("SELECT country_id, country_name FROM Country")
# country_id_map = {name: id for id, name in cursor.fetchall()}


# for _, row in df.iterrows():
#     if pd.notna(row['country']):
#         countries = [c.strip() for c in str(row['country']).split(",")]
#         for country in countries:
#             if country in country_id_map:
#                 cursor.execute("""
#                     INSERT OR IGNORE INTO ShowCountry (show_id, country_id)
#                     VALUES (?, ?)
#                 """, (row['show_id'], country_id_map[country]))

#testing 
cursor.execute("SELECT COUNT(*) FROM Country")
print(f"Countries: {cursor.fetchone()[0]}")  # Should be ~200

cursor.execute("SELECT COUNT(*) FROM ShowCountry")  
print(f"Show-Country relationships: {cursor.fetchone()[0]}")  # Should be ~20,000

# # all Langs
# all_languages = set()
# for _, row in df.iterrows():
#     if pd.notna(row['language']):
#         languages = [lang.strip() for lang in str(row['language']).split(",")]
#         all_languages.update(languages)  

# print(f"Found {len(all_languages)} unique languages") 

# for language in sorted(all_languages):
#     cursor.execute("INSERT OR IGNORE INTO Language (name) VALUES (?)", (language,))

# cursor.execute("SELECT lang_id, name FROM Language")
# language_id_map = {name: id for id, name in cursor.fetchall()}

# for _, row in df.iterrows():
#     if pd.notna(row['language']):
#         languages = [lang.strip() for lang in str(row['language']).split(",")]
#         for language in languages:
#             if language in language_id_map: 
#                 cursor.execute("""
#                     INSERT OR IGNORE INTO ShowLang (show_id, lang_id)
#                     VALUES (?, ?)
#                 """, (row['show_id'], language_id_map[language]))  


#testing 
cursor.execute("SELECT COUNT(*) FROM Language")
print(f"Languages: {cursor.fetchone()[0]}")  # Should be ~100

cursor.execute("SELECT COUNT(*) FROM ShowLang")  
print(f"Show-Language relationships: {cursor.fetchone()[0]}")  # Should be ~32,000


# Genres code
# all_genres = set()
# for _, row in df.iterrows():
#     if pd.notna(row['genres']):
#         genres = [g.strip() for g in str(row['genres']).split(",")]
#         all_genres.update(genres)

# print(f"Found {len(all_genres)} unique genres")  # Should be ~20-50

# for genre in sorted(all_genres):
#     cursor.execute("INSERT OR IGNORE INTO Genre (type) VALUES (?)", (genre,))

# cursor.execute("SELECT genre_id, type FROM Genre")
# genre_id_map = {name: id for id, name in cursor.fetchall()}

# for _, row in df.iterrows():
#     if pd.notna(row['genres']):
#         genres = [g.strip() for g in str(row['genres']).split(",")]
#         for genre in genres:
#             if genre in genre_id_map:
#                 cursor.execute("""
#                     INSERT OR IGNORE INTO ShowGenre (show_id, genre_id)
#                     VALUES (?, ?)
#                 """, (row['show_id'], genre_id_map[genre]))
#testing
cursor.execute("SELECT COUNT(*) FROM Genre")
print(f"Genres: {cursor.fetchone()[0]}")  # Should be ~50

cursor.execute("SELECT COUNT(*) FROM ShowGenre")  
print(f"Show-Genre relationships: {cursor.fetchone()[0]}")  # Should be ~37,000

# # Director code
# all_directors = set()
# for _, row in df.iterrows():
#     if pd.notna(row['director']):
#         directors = [d.strip() for d in str(row['director']).split(",")]
#         all_directors.update(directors)

# print(f"Found {len(all_directors)} unique directors")  # Should be ~5,000-10,000

# for director in sorted(all_directors):
#     cursor.execute("INSERT OR IGNORE INTO Director (dir_name) VALUES (?)", (director,))

# cursor.execute("SELECT director_id, dir_name FROM Director")
# director_id_map = {name: id for id, name in cursor.fetchall()}

# for _, row in df.iterrows():
#     if pd.notna(row['director']):
#         directors = [d.strip() for d in str(row['director']).split(",")]
#         for director in directors:
#             if director in director_id_map:
#                 cursor.execute("""
#                     INSERT OR IGNORE INTO ShowDirector (show_id, director_id)
#                     VALUES (?, ?)
#                 """, (row['show_id'], director_id_map[director]))

#testing
cursor.execute("SELECT COUNT(*) FROM Director")
print(f"Directors: {cursor.fetchone()[0]}")  # Should be ~8,000

cursor.execute("SELECT COUNT(*) FROM ShowDirector")  
print(f"Show-Director relationships: {cursor.fetchone()[0]}")  # Should be ~16,000
# # Actor code  
# all_actors = set()
# for _, row in df.iterrows():
#     if pd.notna(row['cast']):
#         actors = [a.strip() for a in str(row['cast']).split(",")]
#         all_actors.update(actors)

# print(f"Found {len(all_actors)} unique actors")  # Should be ~20,000-30,000

# for actor in sorted(all_actors):
#     cursor.execute("INSERT OR IGNORE INTO Actor (name) VALUES (?)", (actor,))

# cursor.execute("SELECT actor_id, name FROM Actor")
# actor_id_map = {name: id for id, name in cursor.fetchall()}

# for _, row in df.iterrows():
#     if pd.notna(row['cast']):
#         actors = [a.strip() for a in str(row['cast']).split(",")]
#         for actor in actors:
#             if actor in actor_id_map:
#                 cursor.execute("""
#                     INSERT OR IGNORE INTO ShowActor (show_id, actor_id)
#                     VALUES (?, ?)
#                 """, (row['show_id'], actor_id_map[actor]))
#testing
cursor.execute("SELECT COUNT(*) FROM Actor")
print(f"Actors: {cursor.fetchone()[0]}")  # Should be ~30,000

cursor.execute("SELECT COUNT(*) FROM ShowActor")  
print(f"Show-Actor relationships: {cursor.fetchone()[0]}")  # Should be ~77,000
conn.commit()
conn.close()

 